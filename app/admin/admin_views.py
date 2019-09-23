#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/22 16:43
import datetime

from flask import request
from flask_restful import Resource

from app import db
from app.models import Admin, Role
from app.utils.response import make_response


class AdminListView(Resource):

    def get(self):
        admin_list = Admin.query.join(Role).filter(Role.id == Admin.role_id).order_by(Admin.addtime.desc()).all()
        resp_data = []
        for admin in admin_list:
            role = admin.roles
            resp_data.append({
                'id': admin.id,
                'name': admin.name,
                'pwd': admin.pwd,
                'addtime': str(admin.addtime),
                'role': {
                    'id': role.id,
                    'name': role.name,
                    'authList': [int(auth) for auth in role.auths.split(';')],
                    'addtime': role.addtime
                }
            })
        return make_response(code=0, data=resp_data, msg='Success')

    def post(self):
        params = request.json
        name = params['name']
        pwd = params['password']
        role_id = params['roleId']
        admin = Admin.query.filter_by(name=name).first()
        if admin is None:
            db.session.add(Admin(
                name=name,
                pwd=pwd,
                addtime=datetime.datetime.now(),
                role_id=role_id
            ))
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该管理员已存在!')


class AdminView(Resource):

    def put(self):
        pass

    def delete(self):
        pass


class AdminLoginView(Resource):

    def post(self):
        params = request.json
        name = params['name']
        password = params['password']
        admin = Admin.query.filter_by(name=name).first()
        print(admin)
        if admin is not None:
            if admin.pwd == password:
                return make_response(code=0, msg='Success')
            return make_response(code=1, msg='账号或者密码错误!')
        else:
            return make_response(code=0, msg='该管理员不存在!')
