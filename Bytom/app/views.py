# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-01 15:56:18
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-06 15:11:45
from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
# from flask_login import login_user, logout_user, current_user, login_required
from app import app, mongo
# from app.models import User
# from werkzeug.urls import url_parse
from datetime import datetime

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
	weibo = mongo.db.weibo.find()[:100]
	return render_template('weibo.html',items=weibo)

@app.route('/bilibili')
def bilibili():
	bilibili = mongo.db.bilibili.find()[:100]
	return render_template('bilibili.html',items=bilibili)

@app.route('/jianshu')
def jianshu():
	jianshu = mongo.db.jianshu.find()[:100]
	return render_template('jianshu.html',items=jianshu)


