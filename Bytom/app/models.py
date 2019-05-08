# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-01 15:59:38
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-08 11:58:25
# from app import db

from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from hashlib import md5



class User(UserMixin,db.Model):
	#index表示创建索引
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(64),index=True,unique=True)
	email = db.Column(db.String(120),index=True,unique=True)
	password_hash = db.Column(db.String(128))
	#relationship在一对多的一这一侧定义
							#表示‘多’方面的类
	# posts = db.relationship('Post',backref='author',lazy='dynamic')
	# #https://github.com/Microndgt/The-Flask-Mega-Tutorial/blob/master/The-Flask-Mega-Tutorial/part8.md 详解
	# #左边的用户关注右边的用户
	# #followed 我关注的人
	# followed = db.relationship("User",secondary=followers,primaryjoin=(followers.c.follower_id == id),
	# 																	#followers 是关注我的人
	# 																	#从左侧看右侧 我关注的人 followed
	# 																	#从右侧看左侧 关注我的人 follower
	# secondaryjoin=(followers.c.followed_id == id),backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
	# about_me = db.Column(db.String(140))
	# last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	#打印类的对象
	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self,password):
		self.password_hash = generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.password_hash,password)

	# def avatar(self,size):
	# 	#先转成小写，再转为utf8
	# 	digest = md5(self.email.lower().encode('utf-8')).hexdigest()
	# 	return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
	# 		digest, size)
	# def follow(self,user):
	# 	if not self.is_following(user):
	# 		self.followed.append(user)
	# def unfollow(self,user):
	# 	if self.is_following(user):
	# 		self.followed.remove(user)
	# def is_following(self,user):
	# 	return self.followed.filter(followers.c.followed_id == user.id).count() > 0

	#获取我所关注的用户的文章	
	# def followed_posts(self):
	# 	#这个查询做了个什么事情？
	# 	#先连接查询 把post和被关注的人 两张表连起来 
	# 	followed = Post.query.join(
	# 		followers, (followers.c.followed_id == Post.user_id)).filter(
	# 			followers.c.follower_id == self.id)
	# 	own = Post.query.filter_by(user_id=self.id)
	# 	return followed.union(own).order_by(Post.timestamp.desc())


	#这个函数的功能还不是很能理解
@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

