# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-01 15:56:18
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-13 23:46:22
from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_pymongo import PyMongo,DESCENDING,ASCENDING
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm,RegistrationForm,ResetPasswordRequestForm,ResetPasswordForm
from app import app, mongo,db
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime
from app.email import send_password_reset_email
import re

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
	page = request.args.get('page', 1, type=int)
	count = mongo.db.index.find().count()
	items = Paginate(page,count)
	if items.has_next:
		next_url = url_for('index', page=items.nextnum)
	else:
		next_url = None

	if items.has_prev:
		prev_url = url_for('index', page=items.prevnum)
	else:
		prev_url = None
	index = mongo.db.index.find().sort([('title', DESCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)
	if current_user.is_authenticated:
		collections = eval(current_user.collection)
	else:
		collections = "[]"
	return render_template('index.html',items = index,collections=collections,next_url=next_url,prev_url=prev_url)


@app.route('/weibo')
@login_required
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

	weibo = mongo.db.weibo.find({"content":{"$exists":"true"},"$where":"(this.content.length > 30)"}).sort([('likenum', ASCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)
	info = []
	for one in weibo:
		match = re.search(r"(【.*?】)(.*)(http:.{14})",one['content'])
		if match:
			title = match.group(1)
			describe = match.group(2)
			url = match.group(3)
			data = {
				"title":title,
				"describe":describe,
				"url":url,
				"retweet":one["retweet"],
				"likenum":one["likenum"],
				"commentnum":one["commentnum"],

			}
			info.append(data)
	return render_template('weibo.html',items=info,next_url=next_url,prev_url=prev_url)

@app.route('/bilibili')
@login_required
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
@login_required
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
@login_required
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

@app.route('/github')
@login_required
def github():
	page = request.args.get('page', 1, type=int)
	count = mongo.db.github.find().count()
	items = Paginate(page,count)
	count = mongo.db.github.find().count()
	if items.has_next:
		next_url = url_for('github', page=items.nextnum)
	else:
		next_url = None

	if items.has_prev:
		prev_url = url_for('github', page=items.prevnum)
	else:
		prev_url = None
	github = mongo.db.github.find().sort([('datestamp', ASCENDING)]).skip(PERPAGE*(page-1)).limit(PERPAGE)
	return render_template('github.html',items=github,next_url=next_url,prev_url=prev_url)



@app.route('/login', methods = ['GET', 'POST'])
def login():	
	#如果已经登陆了，就直接去index，不用重复登录	
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		#如果用户名不存在 或者 密码错误,就继续留在login
		if user is None or not user.check_password(form.password.data):
			flash('用户名或者密码错误')
			return redirect(url_for('login'))
		#登录了
		login_user(user,remember = form.remember_me.data)
		#url中是视图函数的名字
		# return redirect(url_for('index'))
		#如果直接进入login页面，登陆后自动跳转到index
		next_page = request.args.get('next')
		#如果登录 URL 没有一个 next 参数
		#如果登录 URL 的 next 参数被设置成了包含域名的完整路径（安全性）
		if not next_page or url_parse(next_page).netloc != "":
			next_page = url_for('index')	
		#以下处理是：如果是先访问的index 但要求登录 登录完后跳转到next
		return redirect(next_page)		

	return render_template('login.html',
		title = 'Sign In',
		form = form,
		)
@app.route('/logout')
def logout():
	logout_user()
	return	redirect(url_for('index'))

@app.route('/register',methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data,collection="[]")
		#手动将输入密码放入数据库中
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = ResetPasswordRequestForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			send_password_reset_email(user)
		flash('Check your email for the instructions to reset your password')
		return redirect(url_for('login'))
	return render_template('reset_password_request.html',
						   title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	user = User.verify_reset_password_token(token)
	if not user:
		return redirect(url_for('index'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		user.set_password(form.password.data)
		db.session.commit()
		flash('Your password has been reset.')
		return redirect(url_for('login'))
	return render_template('reset_password.html', form=form)

@app.route('/collect/<title>')
@login_required
def collect(title):
	if not current_user.is_collected(title):
		current_user.collect(title)
	# db.session.commit()
	flash('收藏成功')
	return redirect(url_for('index'))

@app.route('/uncollect/<title>')
@login_required
def uncollect(title):
	if  current_user.is_collected(title):
		current_user.uncollect(title)
	# db.session.commit()
	flash('取消成功')
	return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	collections = eval(user.collection)

	items = []
	for i in collections:
		items.append(mongo.db.index.find_one({"title":i}))
	print(items)
	return render_template('user.html',user=user,items =items)
