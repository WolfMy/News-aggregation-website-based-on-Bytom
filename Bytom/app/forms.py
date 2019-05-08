# -*- coding: utf-8 -*-
# @Author: TD21forever
# @Date:   2019-05-08 10:52:35
# @Last Modified by:   TD21forever
# @Last Modified time: 2019-05-08 10:52:39
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models import User


class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	password2 = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField("Register")
	#当你以 validate_<filed_name> 的模式添加方法的时候，WTForms会将它们作为自定义验证器
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')
