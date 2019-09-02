#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 22:16
# @site  : https://github.com/SunmoonSan
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Length

from app.models import Admin, Role, Auth, Tag, User


# 登录表单
class LoginForm(FlaskForm):
    account = StringField(
        label='账号',
        validators=[
            DataRequired('账号不能为空')
        ],
        description='账号',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            "required": "required"
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
            "placeholder": "请输入密码！",
            "required": "required"
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


class RegisterForm(FlaskForm):
    name = StringField(
        label='昵称',
        validators=[
            DataRequired('昵称不能为空!')
        ],
        description='昵称',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
        }
    )

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired('邮箱不能为空!')
        ],
        description='邮箱',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "邮箱",
        }
    )

    phone = StringField(
        label='手机',
        validators=[
            DataRequired('手机号码不能为空!'),
            Regexp(''),
            Length(min=11, max=11, message='手机号码长度不正确!')
        ],
        description='手机号码',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '手机',
        }
    )

    password = PasswordField(
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

    pwd_confirm = PasswordField(
        label='再次输入密码',
        validators=[
            DataRequired('密码不能为空!'),
            EqualTo('password', message='两次输入密码不同!')
        ],
        description='再次输入密码',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '密码',
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError('该用户已经存在!')

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError('该邮箱已存在!')

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError('手机号码已经存在!')


class MovieForm(FlaskForm):
    title = StringField(
        label='片名',
        validators=[
            DataRequired('片名不能为空!')
        ],
        description='片名',
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入片名！"
        }
    )

    url = FileField(
        label='文件',
        validators=[
            DataRequired('请上传文件!')
        ],
        description='文件',
    )

    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired('简介不能为空!')
        ],
        description='简介',
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )

    logo = FileField(
        label='封面',
        validators=[
            DataRequired('请上传封面!')
        ],
        description='封面',
    )

    star = SelectField(
        label='星级',
        validators=[
            DataRequired('请选择星级!')
        ],
        coerce=int,
        choices=[(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')],
        description='星级',
        render_kw={
            'class': 'form-control'
        }
    )

    tag_id = SelectField(
        label='标签',
        validators=[
            DataRequired('请选择标签!')
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in Tag.query.all()],
        description='标签',
        render_kw={
            'class': 'form-control'
        }
    )

    area = StringField(
        label='地区',
        validators=[
            DataRequired('请输入地区!')
        ],
        description='地区',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入地区!'
        }
    )

    length = StringField(
        label='片长',
        validators=[
            DataRequired('片长不能为空!')
        ],
        description='片长',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入片长!'
        }
    )

    release_time = StringField(
        label='上映时间',
        validators=[
            DataRequired('上映时间不能为空!')
        ],
        description='上映时间',
        render_kw={
            "class": "form-control",
            "placeholder": "请选择上映时间！",
            "id": "input_release_time"
        }
    )

    submit = SubmitField(
        '添加',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


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
        choices=[(v.id, v.name) for v in Role.query.all()],
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
            DataRequired("标签名不能为空!"),
        ],
        description='标签',
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )

    submit = SubmitField(
        label='添加',
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
        label='编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )
