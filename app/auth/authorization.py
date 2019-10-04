#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/30 09:40
import datetime
import time
from functools import wraps

import jwt
from flask import current_app, request

from app.models import User, Admin
from app.utils.response import make_response


class AdminAuth:

    @staticmethod
    def encode_auth_token(admin):
        """
        生成认证Token
        :param admin:
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=600),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': admin.id,
                    'username': admin.name,
                }
            }
            return jwt.encode(
                payload=payload,
                key=current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as err:
            print(err)

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return:
        """
        try:
            payload = jwt.decode(jwt=auth_token, key=current_app.config['SECRET_KEY'])
            if 'data' in payload and 'id' in payload['data']:
                return payload
        except jwt.ExpiredSignatureError as err:
            print(err)
            return str(err)
        except jwt.InvalidTokenError as err:
            return str(err)

    @classmethod
    def authenticate(cls, admin):
        """
        用户登录, 登录成功返回token, 将登录时间写入数据库,登录失败返回失败原因.
        :param admin: 管理员
        :return:
        """
        token = cls.encode_auth_token(admin=admin)
        return bytes.decode(token)

    @classmethod
    def identify(cls, headers):
        authorization = headers.get('Authorization')
        resp = {'allow_access': False}
        if authorization:
            if authorization.startswith('JWT '):
                token = authorization[4:]
                payload = cls.decode_auth_token(token)
                if isinstance(payload, dict):
                    user_id = payload.get('data')['id']
                    user = User.query.get(user_id)
                    if user is None:
                        resp.update({'msg': '找不到该用户信息'})
                    else:
                        resp.update({'allow_access': True, 'user': user, 'user_id': user_id})
                else:
                    resp.update({'msg': payload})
            else:
                resp.update({'msg': 'token格式不正确'})
        else:
            resp.update({'msg': '没有token信息'})
        return resp
