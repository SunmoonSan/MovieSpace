#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/24 23:32
import datetime

from flask import current_app, session, request
from flask_login import login_user, logout_user
from flask_restful import Resource, reqparse

from app import db
from app.models import User, Userlog
from app.utils.response import make_response

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)


class Register(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)
        email = args['email']
        password = args['password']
        user = User.query.filter_by(email=email).first()
        if user is None:
            user = User(email=email, pwd=password)
            db.session.add(user)
            db.session.commit()
            db.session.add(Userlog(ip=request.remote_addr,
                                   user_id=user.id, addtime=datetime.datetime.now()))
            return make_response(code=0)
        else:
            return make_response(code=1, msg='邮箱已经被注册!')


class Login(Resource):

    def post(self):
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if password == user.pwd:
                login_user(user=user)
                print('login', session)
                # 保存会员登录日志
                db.session.add(Userlog(
                    ip=request.remote_addr,
                    user_id=user.id,
                    addtime=datetime.datetime.now()
                ))
                db.session.commit()
                return make_response(code=0)
            else:
                return make_response(code=1, msg='邮箱或密码不正确!')
        else:
            return make_response(code=1, msg='账号不存在!')


class Logout(Resource):

    def get(self):
        logout_user()
        print('logout', session)
        return make_response(code=0)
