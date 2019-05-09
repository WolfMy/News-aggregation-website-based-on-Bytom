import requests
import time
import os
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from multiprocessing import Pool    

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
driver = webdriver.Chrome(r'/Users/mouyu/Documents/Github/News-aggregation-website-based-on-Bytom/chromedriver')

target = "https://www.instagram.com/yumou0407/?hl=zh-cn"


driver.get(target)

url_set=set([])#set用来unique URL

pic_index = 0

url_set_size = 0

save_dir = './kohachannel/'

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

headers ={ 
    'cookie': 'csrftoken=HwFSbIgDrvrm2pk0ivkPCQb69xZM6oBs; rur=FRC; mid=XNJODQAEAAECuv-2TTPP_0m0Ufz7; urlgen="{\"45.78.70.93\": 25820}:1hODN4:UY3Inl3Q7kcT5iOKCLjE0j3CO5M"',
    'upgrade-insecure-requests':'1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
while(True):
    divs = driver.find_elements_by_class_name('v1Nh3')  #这里最好使用xxxx_by_class_name，我尝试过用xpath绝对路径，但是好像对于页面变化比较敏感

    for u in divs:
        url_set.add(u.find_element_by_tag_name('a').get_attribute('href'))
    print(url_set)

    if len(url_set) == url_set_size: #如果本次页面更新没有加入新的URL则可视为到达页面底端，跳出
        break
    
    url_set_size = len(url_set)
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()#三次滑动，保证页面更新足够
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(3)



#下载图片：
def pic_download(u_download):
    global pic_index
    
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    s = requests.session()
    s.keep_alive = False # 关闭多余连接

    rec = s.get(u_download, headers = headers)

    selector = etree.HTML(rec.content)

    meta = selector.xpath('/html/head/meta[10]')[0]  #使用xpath解析页面

    real_pic_url = meta.get("content").strip()

    pic_extend = real_pic_url[-4:]

    file_name = save_dir + "haki_" + str(pic_index) + ".jpg"

    pic_index += 1

    f = open(file_name,'wb')

    pic_bin = s.get(real_pic_url).content

    f.write(pic_bin)

    f.close()


for url_ in url_set:
    try:
        pic_download(url_)
        print('成功'+str(pic_index))
    except Exception as e:
        print("错误")
        print(e)