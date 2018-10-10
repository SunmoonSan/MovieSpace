#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:59
# @site  : https://github.com/SunmoonSan
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, ValidationError

from app.models import User


# 注册表单
class RegisterForm(FlaskForm):
    name = StringField(
        label='昵称',
        validators=[
            DataRequired('昵称不能为空!')
        ],
        description='昵称',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '昵称'
        }
    )

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired('邮箱不能为空!'),
            Email('邮箱格式不正确!')
        ],
        description='邮箱',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '邮箱'
        }
    )

    phone = StringField(
        label='手机',
        validators=[
            DataRequired('手机号不能为空!'),
            Regexp('1[3458]\\d{9}', message='手机号格式不正确')
        ],
        description='手机',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '手机'
        }
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('密码不能为空!')
        ],
        description='密码',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '密码'
        }
    )

    repwd = PasswordField(
        label='确认密码',
        validators=[
            DataRequired('请输入密码!'),
            EqualTo('pwd', message='两次密码不一致!')
        ],
        description='确认密码',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '确认密码'
        }
    )

    submit = SubmitField(
        label='注册',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '注册'
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError('昵称已经存在!')

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError('邮箱已存在!')

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError('手机号码已经存在!')


# 登录表单
class LoginForm(FlaskForm):
    name = StringField(
        label='账号',
        validators=[
            DataRequired('账户不能为空!')
        ],
        description='帐号',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
        }
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('密码不能为空!')
        ],
        description='密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )

    submit = SubmitField(
        label='登录',
        render_kw={
            "class": "form-control input-lg",
        }
    )


# 用户个人中心表单
class UserProfileForm(FlaskForm):
    name = StringField(
        label='昵称',
        description='帐号',
        render_kw={
            'class': 'form-control',
            'placeholder': '昵称'
        }
    )

    email = StringField(
        label='邮箱',
        description='邮箱',
        render_kw={
            'class': 'form-control',
            'placeholder': '邮箱'
        }
    )

    phone = StringField(
        label='手机号码',
        description='邮箱',
        render_kw={
            'class': 'form-control',
            'placeholder': '手机号码'
        }
    )

    info = TextAreaField(
        label='简介',
        description='简介',
        render_kw={
            'class': 'form-control',
            'rows': 10
        }
    )

    face = FileField(
        label="头像",
        description="头像",
    )

    submit = SubmitField(
        label='保存修改',
        render_kw={
            'class': 'btn btn-success'
        }
    )


class PasswordForm(FlaskForm):
    old_password = StringField(
        label='旧密码',
        validators=[
            DataRequired('密码不能为空!')
        ],
        description='旧密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '旧密码'
        }
    )

    new_password = StringField(
        label='新密码',
        validators=[
            DataRequired('密码不能为空!')
        ],
        description='新密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '旧密码'
        }
    )

    submit = SubmitField(
        label='修改',
        render_kw={
            'class': 'btn btn-success'
        }
    )
