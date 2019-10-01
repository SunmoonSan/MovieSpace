#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/24 23:32
import datetime

from flask import request, app, current_app
from flask_login import login_user, logout_user
from flask_restful import Resource, reqparse, output_json

from app import db
from app.auth.auth_views import Auth
from app.models import User, Userlog
from app.utils.response import make_response

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)


class DBPool:

    def __init__(self):
        pass


class Register(Resource):

    def post(self):
        args = parser.parse_args()
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
                # 保存会员登录日志
                db.session.add(Userlog(
                    ip=request.remote_addr,
                    user_id=user.id,
                    addtime=datetime.datetime.now()
                ))
                db.session.commit()
                token = Auth.authenticate(email=email, password=password)
                return make_response(code=0, data={'token': token}, msg='Success')
            else:
                return make_response(code=1, msg='邮箱或密码不正确!')
        else:
            return make_response(code=1, msg='账号不存在!')


class Logout(Resource):

    def get(self):
        logout_user()
        return make_response(code=0)


class ProfileView(Resource):

    def get(self):
        resp = Auth.identify(request.headers)
        if not resp['allow_access']:
            return make_response(code=1, msg=resp['msg'])

        user_id = resp['user_id']

        user = User.query.get(user_id)
        if user is not None:
            return make_response(code=0, data={
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
                'info': user.info,
                'avatar': user.face
            }, msg='Success')
        return make_response(code=1, msg='用户不存在')

    def put(self, user_id):
        params = request.json
        user = User.query.get(user_id)
        if user is not None:
            user.email = params['email']
            user.name = params['name']
            user.phone = params['phone']
            user.info = params['info']
            user.face = params['avatar']
            db.session.add(user)
            db.session.commit()
            return make_response(code=0, msg='Success')
        return make_response(code=1, msg='用户不存在')


class PasswordModifyView(Resource):

    def put(self):

        # resp = Auth.identify(request.headers)
        # print(resp)
        # if not resp['allow_access']:
        #     return make_response(code=1, msg=resp['msg'])

        # user_id = resp['user_id']
        user_id = 17

        params = request.json
        old_pwd = params['oldpwd']
        new_pwd = params['newpwd']

        user = User.query.get(user_id)
        if user.pwd == old_pwd:
            user.pwd = new_pwd
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='旧密码输入不正确')
