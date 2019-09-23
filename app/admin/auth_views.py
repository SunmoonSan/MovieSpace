#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/22 16:58
from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from app import db
from app.models import Auth
from app.utils.response import make_response


class AuthListView(Resource):

    def get(self):
        auth_list = Auth.query.all()
        resp_data = []
        for auth in auth_list:
            resp_data.append({
                'id': auth.id,
                'name': auth.name,
                'url': auth.url,
                'addtime': str(auth.addtime)
            })
        return make_response(code=0, data=resp_data, msg='Success')

    def post(self):
        params = request.json
        name = params['name']
        url = params['url']
        auth = self._is_name_existed(name=name)
        if auth is None:
            db.session.add(Auth(
                name=name,
                url=url
            ))
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该权限已存在')

    @staticmethod
    def _is_name_existed(name):
        try:
            auth = Auth.query.filter_by(name=name).first()
            if auth:
                return auth
        except Exception as err:
            print('[error]:', err)


class AuthOfRoleView(Resource):

    def post(self):
        params = request.json
        auth_ids = params['authIds']
        auth_list = Auth.query.filter(Auth.id.in_(auth_ids)).all()
        resp_data = []
        for auth in auth_list:
            resp_data.append({
                'id': auth.id,
                'name': auth.name,
            })
        return make_response(code=0, data=resp_data, msg='Success')


class AuthView(Resource):

    def put(self, auth_id):
        params = request.json
        auth = self._is_id_existed(auth_id=auth_id)
        if auth is not None:
            db.session.query(Auth).filter_by(id=auth_id).update({
                'name': params['name'],
                'url': params['url']
            })
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该权限不存在!')

    def delete(self, auth_id):
        auth = self._is_id_existed(auth_id=auth_id)
        if auth is not None:
            db.session.delete(auth)
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该权限不存在!')

    @staticmethod
    def _is_id_existed(auth_id):
        try:
            auth = Auth.query.get(auth_id)
            if auth:
                return auth
        except Exception as err:
            print('[error]:', err)
