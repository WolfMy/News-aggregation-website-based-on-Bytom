# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-04-27 19:31:14
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-04 15:57:35
import requests
from bs4 import BeautifulSoup
import json
import pymongo

client = pymongo.MongoClient(host='127.0.0.1',port=27017)
Bytom_info_test = client['bytom_info']
huodongxing = Bytom_info_test['huodongxing']
bilibili = Bytom_info_test['bilibili']
jianshu = Bytom_info_test['jianshu']
github = Bytom_info_test['github']




# url = "https://twitter.com/Bytom_Official"
# headers = {
	
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
# 	'Referer': 'https://twitter.com/Bytom_Official'
# }
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# print(soup.select('span.FullNameGroup'))


#===========================================================GITHUB OK==========================
# url = 'https://github.com/Bytom/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# titles = [i.text.strip() for i in soup.select('h3.wb-break-all')]
# describes = [k.text.strip() for k in soup.select('p.col-9')]
# language = [j.text.strip() for j in soup.select("span.ml-0 span[itemprop='programmingLanguage']")]
# urls = [url+i.get('href') for i in soup.select('a[itemprop="name codeRepository"]')]
# timestamp = [i.get('datetime').split("T")[0] for i in soup.select("relative-time")]
# data=[]
# for one in zip(titles,describes,language,urls,timestamp):
# 	data.append(
# 	{
# 		"title": one[0],
# 		"describe": one[1],
# 		"language": one[2],
# 		"urls":one[3],
# 		"timestamp":one[4]
# 	})
# # print(data)
# # data = json.dumps(data)
# for one in data:
# 	github.insert_one(one)

#======================================================简书 OK===============================================
# urls = ['https://www.jianshu.com/u/0ff83f048a95?order_by=shared_at&page=%s' %i for i in range(1,6)]
# url = urls[0]
# headers = {
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
# }
# BASEURL = "https://www.jianshu.com/"
# for url in urls:
# 	response = requests.get(url,headers=headers)
# 	soup = BeautifulSoup(response.text,'lxml')
# 	items = soup.select('li[data-note-id]')
# 	for one in items:
# 		title = one.find(class_='title').text.strip()
# 		link = one.find(class_='title').get('href')
# 		describe = one.find(class_="abstract").text.strip()
# 		playnum = one.select('a[target="_blank"]')[-2].text.strip()
# 		commentnum = one.select('a[target="_blank"]')[-1].text.strip()
# 		favorite = one.find(class_="meta").find('span').text.strip()
# 		timestamp = one.find(class_="time").get("data-shared-at").split('T')[0]
# 		data = {
# 	 		"title": title,
# 	 		"url": BASEURL+link,
# 	 		"describe": describe,
# 	 		"playnum":playnum,
# 	 		"commentnum":commentnum,
# 	 		"favorite":favorite,
# 	 		'timestamp':timestamp
# 	 	}
# 		jianshu.insert_one(data)		




#==============================================BILIBILI OK============================================
# url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=340186989&pagesize=30&tid=0&page=1&keyword=&order=pubdate'
# BASEURL = "https://www.bilibili.com/video/"
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
# 	'Referer': 'https://space.bilibili.com/340186989/video',
# 	'Accept': 'application/json, text/plain, */*'
# }
# response = requests.get(url,headers=headers)
# wb_data = json.loads(response.text)
# res = wb_data['data']['vlist']
# for one in res:
# 	data = {
# 	'title':one['title'],
# 	'url':BASEURL+'av'+str(one['aid']),
# 	'author':one['author'],
# 	'commentnum':one['comment'],
# 	'playnum':one['play'],
# 	'favorite':one["favorites"]
# 	}
# 	print(data)
# 	bilibili.insert_one(data)


#=============================================活动行OK=======================================================
# headers={
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
# }
# BASEURL = "https://www.huodongxing.com/"
# url = "https://www.huodongxing.com/people/7602880561672?type=pub"
# response = requests.get(url,headers=headers)
# soup = BeautifulSoup(response.text,'lxml')
# infos = soup.select("div.media-body")
# hrefs = soup.select("a.media")
# urls = []
# for href in hrefs:
# 	urls.append(href.get('href'))
# i = 0
# for one in infos:
# 	title = one.find('h3').text.strip() 
# 	datestamp = one.find_all('div')[0].text.strip() 
# 	place = one.find_all('div')[1].text.strip()
# 	data = {
# 		"title":title,
# 		"url":BASEURL+urls[i],
# 		"datestamp":datestamp,
# 		"place":place

# 	}
# 	i+=1
# 	huodongxing.insert_one(data)