#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/22 16:58
from flask import request
from flask_restful import Resource

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


class AuthView(Resource):

    def put(self):
        pass

    def delete(self):
        pass
