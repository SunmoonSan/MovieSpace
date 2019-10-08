#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/8 18:54
from flask import request, current_app
from flask_restful import Resource

from app.models import User
from app.utils.response import make_response
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, \
    BadSignature


def generate_auth_token(uid, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
    })


class AdminToken(Resource):

    def post(self):
        params = request.json
        email = params.get('email')
        password = params.get('password')
        user = User.query.filter_by(email=email).first()
        if user is not None:
            if user.pwd == password:
                token = generate_auth_token(user.id, 7200)
                return {'token': token.decode('ascii')}, 200
            else:
                return {'code': 1, 'msg': '账号或密码错误'}, 200

        else:
            return {'msg': 'not found'}, 404
