# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-03 22:27:05
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-08 10:46:34
import os
class Config:
	#首先去读取环境变量的值，如果没有，则使用硬编码字符串作为替代
	#当你开发这个应用的时候，没有太高的安全需求，所以你可以直接使用这个硬编码字符串。但是如果应用部署在生产服务器上，我将会在环境变量中设置相应的值以保证安全
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	CSRF_ENABLED = True#跨站点请求伪造保护
	basedir = os.path.abspath(os.path.dirname(__file__))
	#数据库文件的路径
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
