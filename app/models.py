#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 22:32
# @site  : https://github.com/SunmoonSan
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)


# 用户
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)  # 昵称, 唯一约束
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱, 唯一约束
    phone = db.Column(db.String(11), unique=True)  # 手机号, 唯一约束
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像, 唯一约束

    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())  # 添加时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符

    userlogs = db.relationship('Userlog', backref='users')  # 会员日志外键关系
    comments = db.relationship('Comment', backref='users')
    moviecols = db.relationship('Moviecol', backref='users')

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = 'userlogs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 外键
    ip = db.Column(db.String(100))  # IP地址

    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Userlog %r>" % self.id


# 标签
class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)  # 标签名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    movies = db.relationship('Movie', backref='tags')

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)  # 电影名称
    url = db.Column(db.String(255), unique=True)  # 电影地址
    info = db.Column(db.Text)  # 电影介绍
    logo = db.Column(db.String(255))  # 电影封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量

    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 电影长度
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    comments = db.relationship('Comment', backref='movies')
    moviecols = db.relationship('Moviecol', backref='movies')

    def __repr__(self):
        return "<Movie %r>" % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = 'previews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)  # 上映预告标题
    logo = db.Column(db.String(255), unique=True)  # 封面logo
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)  # 评论内容
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 所属用户


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecols'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Moviecol %r>" % self.id


"""
#####################
权限及角色数据模型设计 #
#####################
"""


# 权限
class Auth(db.Model):
    __tablename__ = 'auths'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)  # 权限
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 角色权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    admins = db.relationship('Admin', backref='roles')

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    adminlogs = db.relationship('Adminlog', backref='admins')
    oplogs = db.relationship('Oplog', backref='admins')

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = 'adminlogs'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())  # 登录时间

    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))  # 所属管理员

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = 'oplogs'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))  # 操作IP
    reason = db.Column(db.String(600))  # 操作缘由
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())  # 操作时间

    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))  # 所属管理员

    def __repr__(self):
        return "<Oplog %r>" % self.id


if __name__ == '__main__':
    db.create_all()
