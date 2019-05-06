# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-01 15:55:45
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-06 14:05:52
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
import os


#__name__是目前正在使用的python模块的名字
#app变量是Flask类的一个实例，它是app包的一个成员
app = Flask(__name__)
#告知Flask读取并且应用配置
# app.config.from_object(Config)
#创建数据库对象
app.config['MONGO_DBNAME'] = 'bytom_info'
app.config["MONGO_URI"] = "mongodb://localhost:27017/bytom_info"
mongo = PyMongo(app)
bootstrap = Bootstrap(app)
# migrate = Migrate(app,db)
#从app包导入views模块 views.py

#Flask-Login 需要知道哪个视图允许用户登录
# login_manager = LoginManager(app)
#login 是登录视图的函数名·
#说明 login 是来处理登录的视图函数 这个不是很懂
# login_manager.login_view = 'login'


#为什么routes模块在最底下导入？
#目的是避免循环导入
#这里的app是app包
from app import views
