#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/22 23:03
import datetime

from flask import request
from flask_restful import Resource

from app import db
from app.models import Role
from app.utils.response import make_response


class RoleListView(Resource):

    def get(self):
        role_list = Role.query.all()
        resp_data = []
        for role in role_list:
            print(role)
            print(role.admins)
            print(role.auths)
            resp_data.append({
                'id': role.id,
                'name': role.name,
                'authList': role.auths.split(';'),
                'addtime': str(role.addtime)
            })
        return make_response(code=0, data=resp_data, msg='Success')

    def post(self):
        params = request.json
        name = params['name']
        auth_list = params['authList']
        role = self._is_name_existed(name=name)
        if role is None:
            db.session.add(Role(
                name=name,
                auths=';'.join([str(auth) for auth in auth_list]),
                addtime=datetime.datetime.now()
            ))
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该角色已存在!')

    @staticmethod
    def _is_name_existed(name):
        try:
            role = Role.query.filter_by(name=name).first()
            if role:
                return role
        except Exception as err:
            print('[error]:', err)


class RoleView(Resource):

    def put(self):
        pass

    def delete(self):
        pass
