# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-04-27 19:31:14
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-13 16:37:23
import requests
from bs4 import BeautifulSoup
import json
import pymongo
import re
from lxml import etree
client = pymongo.MongoClient(host='127.0.0.1',port=27017)
Bytom_info_test = client['bytom_info']
huodongxing = Bytom_info_test['huodongxing']
bilibili = Bytom_info_test['bilibili']
jianshu = Bytom_info_test['jianshu']
github = Bytom_info_test['github']
weixin = Bytom_info_test['weixin']
index = Bytom_info_test['index']


# import twitterpastcrawler

# crawler = twitterpastcrawler.TwitterCrawler(
# 							query="#bytom", # searches for tweets that respond to the query, "#haiku"
# 							output_file="haiku.csv" # outputs results to haiku.csv
# 						)

# crawler.crawl() # commences the crawl




# url = "https://twitter.com/Bytom_Official"
# headers = {
	
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
# 	'Referer': 'https://twitter.com/Bytom_Official'
# }
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# print(soup.select('span.FullNameGroup'))


# ===========================================================GITHUB OK==========================
# url = 'https://github.com/Bytom/'
# BASEURL = 'https://github.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# titles = [i.text.strip() for i in soup.select('h3.wb-break-all')]
# describes = [k.text.strip() for k in soup.select('p.col-9')]
# language = [j.text.strip() for j in soup.select("span.ml-0 span[itemprop='programmingLanguage']")]
# urls = [BASEURL+i.get('href') for i in soup.select('a[itemprop="name codeRepository"]')]
# timestamp = [i.get('datetime').split("T")[0] for i in soup.select("relative-time")]
# data=[]
# for one in zip(titles,describes,language,urls,timestamp):
# 	data.append(
# 	{
# 		"title": one[0],
# 		"describe": one[1],
# 		"language": one[2],
# 		"url":one[3],
# 		"timestamp":one[4],
# 		"datasrc":"GITHUB"
# 	})
# print(data)
# # data = json.dumps(data)
# # for one in data:
# # 	github.insert_one(one)
# for one in data:
# 	index.insert_one(one)
# #======================================================简书 OK===============================================
# urls = ['https://www.jianshu.com/u/0ff83f048a95?order_by=shared_at&page=%s' %i for i in range(1,6)]
# url = urls[0]
# headers = {
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
# }
# BASEURL = "https://www.jianshu.com"
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
# 			"title": title,
# 			"url": BASEURL+link,
# 			"describe": describe,
# 			"playnum":playnum,
# 			"commentnum":commentnum,
# 			"favorite":favorite,
# 			'timestamp':timestamp,
# 			"datasrc":"简书"

# 		}
# 		print(data)
# 		# jianshu.insert_one(data)
# 		index.insert_one(data)		





# #==============================================BILIBILI OK============================================
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
# 	'favorite':one["favorites"],
# 	"datasrc":"Bilibili"

# 	}
# 	print(data)
# 	# bilibili.insert_one(data)
# 	index.insert_one(data)



# #=============================================活动行OK=======================================================
# headers={
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
# }
# BASEURL = "https://www.huodongxing.com/"
# url = "https://www.huodongxing.com/people/7602880561672?type=pubdate"
# response = requests.get(url,headers=headers)
# soup = BeautifulSoup(response.text,'lxml')
# infos = soup.select("div.media-body")
# hrefs = soup.select("a.media")
# print(hrefs)
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
# 		"place":place,
# 		"datasrc":"活动行"
# 	}
# 	i+=1
# 	# huodongxing.insert_one(data)
# 	index.insert_one(data)

# 	




# url = "http://mp.weixin.qq.com/profile?src=3&timestamp=1557729823&ver=1&signature=TsSAnpZ-LLwuruwGPfOl4ks6SKN6ER4htPCg6wtsXIE1*2gPwM7Vtas2CuzCAwFPHam3kK8MuyffPMiml*yLew=="
# headers={
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
# }
# BASEURL = "https://mp.weixin.qq.com"
# respond = requests.get(url,headers=headers)
# soup = BeautifulSoup(respond.text,'lxml')
# data = soup.find_all('script',type="text/javascript")[-1]
# data = data.text
# match = re.search("var msgList = (.*)};",data)
# string = match.group(1)+'}'
# res = json.loads(string)
# alist = ['/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKftN*xFGPU3edU-srMYnVitlFs5gLpmOBf0rYbOAT3VYiUe8HWI4vBpWJz105bO6NS2TIqGt1juzga3Yr8e4SC0=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKftN*xFGPU3edU-srMYnViumRfIleFMMXkpAIZALnZEYBPNObKr08JZl4fAC87QzPwGPcXEgpwgZ9AI50U**k-s=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKaTKqDWSaNi33K--oDlL38UxvS2qg-czD967RXPRmh1fuWTGTgQQ9tsqdP3EEGT87besB-3QW-wBxQfQ*H0I4Mg=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKaTKqDWSaNi33K--oDlL38XOadQ0qxOfSHtGA1q4ApFCL5161qRrI*rZwWo0SihYsR9K8Pg9py9G4cvCkDFa7Uc=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKQtU8HedUgELmh6yHdLqs0-chQRgXQc-GAmp6qaIkE5PJIsYdQAaOl77TxAwRUa46M-UTFx3ARLb*II3-n9gf34=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKbg9x7bRVjdAx7M*AVdMBMDRYwPjSRWprSDlB-8KPXKmzKuB5QQf1erR-PJSPLYcAGwBTL7G2c3utgEpjqHCa04=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKW-ufpS8QleD5Wj0I7y42BWxLj0rnYdcG8N80d*hqStrjQQ9Klqec2Dih6deBuUJ-MCSm8VJfyWGFJW6vSboLIU=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKTw3Wqeux6HerxMaKoFcrOfJAN5T8YD2bfWDMCzA*wzCTPasLoLoTpsYsQ2aIs89kZpT9-KvyYfb1loMcPN61K8=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKd2Pi-SxcG2Zzw5w*6d28vUnAjgBycyujJJ*2AifyeVHeDpOY*-If0An0FlU7IIr5jmiWV1GLOGd-2X0PD-*dBw=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKRXwwE3gYewKAWvws6TVLaMOObwwyIw4qyU7eZJPfLSdTGvj2UGcj5HwtKbz1HMajoOk5j*XeQYgwbMQKTPfmBc=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKT9cP3tPiCUAHBe5GgObNBhEStL22q4njVVouGypQbZdBb0vtms1FtIx1iQOOQJ-B-Qc-s5NqbXd2zkUtdhrr8c=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKT9cP3tPiCUAHBe5GgObNBhEStL22q4njVVouGypQbZdBb0vtms1FtIx1iQOOQJ-B-Qc-s5NqbXd2zkUtdhrr8c=',
# 		'/s?timestamp=1557731092&src=3&ver=1&signature=qzZFrR2Tu8BU0J5MaqyWK0cuP2h9lzFd2*S7Y8js-7OvOvyr0uiARR8*o1YWtQY3385VRqoFsDcMyiWOIfPsKet9VcpGrUEjeuFtpI17bOTZrTnfCC*K5ZLCwvY6XiXmmIGEwnfR4dthnRKNXDA4VCmSAvCQ4vvWWdE0cge7xy4=']

# for i in range(len(alist)):
# 	alist[i] = BASEURL+alist[i]
# print(alist[i])
# j=0
# for i in res['list']:
# 	title = i['app_msg_ext_info']["title"]
# 	url = i['app_msg_ext_info']["content_url"]
# 	data = {

# 		"title":title,
# 		"url":alist[j]
# 	}
# 	j+=1
	# weixin.insert_one(data)


headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
	}
url = "https://weixin.sogou.com/weixin?query=%E6%AF%94%E5%8E%9F%E9%93%BEBytom&type=2&page=1"

res = requests.get(url,headers=headers)
print(res.text)
res = etree.HTML(res.text)
print(res.text)