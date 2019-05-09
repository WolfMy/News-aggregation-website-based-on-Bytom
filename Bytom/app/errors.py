# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-08 10:56:23
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-08 10:56:28
from flask import render_template
from app import app,db

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'),404

@app.errorhandler(500)
def not_found_error(error):
	db.session.rollback()
	return render_template('500.html'),500

