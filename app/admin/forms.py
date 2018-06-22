#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 22:16
# @site  : https://github.com/SunmoonSan
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from app.models import Admin, Role, Auth


class LoginForm(FlaskForm):
    account = StringField(
        label='账号',
        validators=[
            DataRequired('账号不能为空')
        ],
        description='账号',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired("密码不能为空")
        ],
        description='密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在!")


class RoleForm(FlaskForm):
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired('角色名称不能为空!')
        ],
        description='角色名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入角色名称!'
        }
    )

    auths = SelectMultipleField(
        label='权限列表',
        validators=[
            DataRequired('权限列表不能为空!')
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in Auth.query.all()],
        description='权限列表',
        render_kw={
            'class': 'form-control'
        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class AdminForm(FlaskForm):
    name = StringField(
        label='管理员名称',
        validators=[
            DataRequired("管理员名称不能为空!")
        ],
        description="管理员名称",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理员名称!'
        }
    )

    pwd = PasswordField(
        label="管理员密码",
        validators=[
            DataRequired("管理员密码不能为空!")
        ],
        description="管理员密码",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理员名称!'
        }
    )

    repwd = PasswordField(
        label="管理员重复密码",
        validators=[
            DataRequired("管理员重复密码不能为空!"),
            EqualTo('pwd', message='两次密码不一致!')
        ],
        description="管理员密码",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理员名称!'
        }
    )

    role_id = SelectField(
        label='所属角色',
        coerce=int,
        choices=[(v.id, v,name) for v in Role.query.all()],
        render_kw={
            'class': 'form-control'
        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class TagForm(FlaskForm):
    name = StringField(
        label='名称',
        validators=[
            DataRequired("标签名不能为空!")
        ],
        description='标签',
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )

    submit = SubmitField(
        '添加',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class AuthForm(FlaskForm):
    name = StringField(
        label='权限名称',
        validators=[
            DataRequired('权限名称不能为空!')
        ],
        description='权限名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入权限名称!'
        }
    )

    url = StringField(
        label='权限地址',
        validators=[
            DataRequired('权限地址不能为空!')
        ],
        description='权限地址',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入权限地址!'
        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )