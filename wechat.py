# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-08 00:32:03
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-08 00:59:28
import functools

import aiohttp
import asyncio
import re
from urllib.parse import quote

import xlwt
from pyquery import PyQuery
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options


def cal_time(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        func(self)
        end = time.time()
        print('{fun} time is {time}'.format(fun=func.__name__, time=end - start))

    return wrapper


class WechatSpider:

    def __init__(self, *args):
        self.account_name = args
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
        self.excel_head = ['时间', '文章标题', '文章地址', '文章简介']
        self.semaphore = asyncio.Semaphore(10)

    @staticmethod
    def get_target_url(sogou_html):
        doc = PyQuery(sogou_html)
        return doc('div[class="txt-box"] p[class="tit"] a').attr('href')

    @staticmethod
    def parse_wechat_html(wechat_html):
        doc = PyQuery(wechat_html)
        articles = doc('div[class="weui_media_box appmsg"]')
        result_list = []
        if articles:
            for article in articles.items():
                # 获取标题
                title = article('h4[class="weui_media_title"]').text()
                # 获取标题url
                url = 'http://mp.weixin.qq.com' + article('h4[class="weui_media_title"]').attr('hrefs')
                # 获取概要内容
                summary = article('.weui_media_desc').text()
                # 获取文章发表时间
                date = article('.weui_media_extra_info').text()
                # 获取文章图片url
                style = article('.weui_media_hd').attr('style')
                pic_url = re.findall('.*?url\((.*?)\)', style)

                result_list.append({
                    'title': title.replace('原创', '').strip(),
                    'url': url,
                    'summary': summary,
                    'date': date.replace('原创', '').strip(),
                    'pic_url': pic_url[0] if pic_url else 'parse pic_url failed'
                })

        return result_list

    @staticmethod
    def get_chrome_result(target_url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='‪C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        driver.get(target_url)
        return driver.execute_script("return document.documentElement.outerHTML")

    @staticmethod
    def excel_style():
        style = xlwt.XFStyle()
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
        style.alignment = alignment

        return style

    def write_to_excel(self, result, name):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1')
        col_1 = sheet.col(0)
        col_2 = sheet.col(1)
        col_3 = sheet.col(2)
        col_4 = sheet.col(3)
        col_1.width = 256 * 18
        col_2.width = 256 * 45
        col_3.width = 256 * 30
        col_4.width = 256 * 150

        for index, head_name in enumerate(self.excel_head):
            sheet.write(0, index, head_name, WechatSpider.excel_style())

        for index, item in enumerate(result):
            sheet.write(index + 1, 0, item['date'], WechatSpider.excel_style())
            sheet.write(index + 1, 1, item['title'])
            sheet.write(index + 1, 2, item['url'])
            sheet.write(index + 1, 3, item['summary'])

        wbk.save('{name}_{date}.xls'.format(name=name, date=time.strftime('%Y-%m-%d')))

    async def get_gzh_info(self, url, name):
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as res:
                    if res.status == 200:
                        text = await res.text()
                        target_url = WechatSpider.get_target_url(text)
                        wechat_html = WechatSpider.get_chrome_result(target_url)
                        result = WechatSpider.parse_wechat_html(wechat_html)
                        self.write_to_excel(result, name)

    @cal_time
    def run(self):
        assert self.account_name, 'WechatSpider初始化至少提供一个公众号名字'
        loop = asyncio.get_event_loop()
        tasks = []
        for name in self.account_name:
            url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query=%s&ie=utf8&_sug_=n&_sug_type_=' % quote(
                name)
            tasks.append(asyncio.ensure_future(self.get_gzh_info(url, name)))

        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()


if __name__ == '__main__':
    WechatSpider('上海发布').run()