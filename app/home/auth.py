#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/10 00:10
from flask import current_app
from flask_restful import Resource, reqparse

from app import db
from app.models import User
from app.utils.response import make_response

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)


class Register(Resource):

    def post(self):
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        user = User.query.filter_by(email=email).first()
        if user is None:
            db.session.add(User(email=email, pwd=password))
            db.session.commit()
            return make_response(code=0)
        else:
            return make_response(code=1, msg='邮箱已经被注册!')