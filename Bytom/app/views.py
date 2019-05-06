# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-01 15:56:18
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-07 01:29:52
from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_pymongo import PyMongo,DESCENDING,ASCENDING
# from flask_login import login_user, logout_user, current_user, login_required
from app import app, mongo
# from app.models import User
# from werkzeug.urls import url_parse
from datetime import datetime

PERPAGE=20

class Paginate:
	def __init__(self, page,total):
		self.total = total
		#总共的页数
		self.pages = int(self.total / PERPAGE)

		if self.total % PERPAGE != 0:
			self.pages += 1
		if page == -1:
			self.page = self.pages
		else:
			#当前的page为传入的参数page
			self.page = page
		if self.page == 1:
			self.has_prev = False
		else:
			self.has_prev = True
		#如果当前的页面大于等于总页数
		if self.page >= self.pages:
			self.has_next = False
		else:
			self.has_next = True
		self.next_num = self.page + 1
		self.per_page = PERPAGE
		self.prev_num = self.page - 1
	@property
	def nextnum(self):
		return self.next_num
	@property
	def prevnum(self):
		return self.prev_num
	@property
	def weibos(self):
		
		return current_weibo

@app.route('/')
@app.route('/index')
def index():
	bilibili = mongo.db.bilibili.find()[:100]
	github =  mongo.db.github.find()[:100]
	huodongxing =  mongo.db.huodongxing.find()[:100]
	jianshu = mongo.db.jianshu.find()[:100]

	return render_template('index.html',items=bilibili)

@app.route('/weibo')
def weibo():
	page = request.args.get('page', 1, type=int)
	#总共的数据量
	count = mongo.db.weibo.find().count()
	items = Paginate(page,count)
	if items.has_next:
		next_url = url_for('weibo', page=items.nextnum)
	else:
		next_url = None

	if items.has_prev:
		prev_url = url_for('weibo', page=items.prevnum)
	else:
		prev_url = None

	weibo = mongo.db.weibo.find({"content":{"$exists":"true"},"$where":"(this.content.length > 30)"}).sort([('_id', DESCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)

	return render_template('weibo.html',items=weibo,next_url=next_url,prev_url=prev_url)

@app.route('/bilibili')
def bilibili():                              
	page = request.args.get('page', 1, type=int)
	count = mongo.db.bilibili.find().count()
	items = Paginate(page,count)
	if items.has_next:
		next_url = url_for('bilibili', page=items.nextnum)
	else:
		next_url = None
	if items.has_prev:
		prev_url = url_for('bilibili', page=items.prevnum)
	else:
		prev_url = None
	bilibili = mongo.db.bilibili.find().sort([('playnum', DESCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)
	return render_template('bilibili.html',items=bilibili,next_url=next_url,prev_url=prev_url)

@app.route('/jianshu')
def jianshu():
	page = request.args.get('page', 1, type=int)
	count = mongo.db.jianshu.find().count()
	items = Paginate(page,count)
	if items.has_next:
		next_url = url_for('jianshu', page=items.nextnum)
	else:
		next_url = None
	if items.has_prev:
		prev_url = url_for('jianshu', page=items.prevnum)
	else:
		prev_url = None
	jianshu = mongo.db.jianshu.find().sort([('timestamp',DESCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)	
	return render_template('jianshu.html',items=jianshu,next_url=next_url,prev_url=prev_url)

@app.route('/huodongxing')
def huodongxing():
	page = request.args.get('page', 1, type=int)
	count = mongo.db.huodongxing.find().count()
	items = Paginate(page,count)
	count = mongo.db.huodongxing.find().count()
	if items.has_next:
		next_url = url_for('huodongxing', page=items.nextnum)
	else:
		next_url = None

	if items.has_prev:
		prev_url = url_for('huodongxing', page=items.prevnum)
	else:
		prev_url = None
	huodongxing = mongo.db.huodongxing.find().sort([('datestamp', ASCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)
	return render_template('huodongxing.html',items=huodongxing,next_url=next_url,prev_url=prev_url)


