# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-01 15:59:38
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-03 23:12:55
# from app import db



# class Website(db.Model):
# 	id = db.Column(db.Integer,primary_key=True)
# 	name = db.Column(db.String(64),index=True,unique=True)
# 	infos = db.relationship('Info',backref='dad',lazy='dynamic')

# class Info(db.Model):
# 	id = db.Column(db.Integer,primary_key=True)
# 	url = db.Column(db.String(140)) 
# 	timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
# 	siteid = db.Column(db.Integer,db.ForeignKey('website.id'))#自动引用user表中id的值