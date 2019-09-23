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
            return Role.query.filter_by(name=name).first()
        except Exception as err:
            print('[error]:', err)


class RoleView(Resource):

    def put(self, role_id):
        parmas = request.json
        role = self._is_id_existed(role_id=role_id)
        if role is not None:
            db.session.query(Role).filter(id=role_id).update({
                'name': parmas['name'],
                'auths': ';'.join(parmas['authList'])
            })
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该角色不存在!')

    def delete(self, role_id):
        role = self._is_id_existed(role_id=role_id)
        if role is not None:
            db.session.delete(role)
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该角色不存在!')

    @staticmethod
    def _is_id_existed(role_id):
        try:
            return Role.query.get(role_id).first()
        except Exception as err:
            print('[error]', err)
