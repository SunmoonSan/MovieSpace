#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/24 18:56
from flask_restful import Resource

from app.models import Adminlog, Admin, Oplog, Userlog, User
from app.utils.response import make_response


class AdminLogView(Resource):

    def get(self):
        log_list = Adminlog.query.join(
            Admin
        ).filter(
            Adminlog.admin_id == Admin.id
        ).order_by(
            Adminlog.addtime.desc()
        ).all()

        resp_data = []
        for log in log_list:
            admin = log.admins
            resp_data.append({
                'id': log.id,
                'ip': log.ip,
                'addtime': str(log.addtime),
                'admin': {
                    'id': admin.id,
                    'name': admin.name
                }
            })
        return make_response(code=0, data=resp_data, msg='Success')


class UserLogView(Resource):

    def get(self):
        log_list = Userlog.query.join(
            User
        ).filter(
            Userlog.user_id == User.id
        ).order_by(
            Userlog.addtime.desc()
        ).all()

        resp_data = []
        for log in log_list:
            user = log.users
            resp_data.append({
                'id': log.id,
                'ip': log.ip,
                'addtime': str(log.addtime),
                'user': {
                    'id': user.id,
                    'name': user.name
                }
            })
        return make_response(code=0, data=resp_data, msg='Success')


class OpLogView(Resource):

    def get(self):
        log_list = Oplog.query.join(
            Admin
        ).filter(
            Oplog.admin_id == Admin.id
        ).order_by(
            Oplog.addtime.desc()
        ).all()

        resp_data = []
        for log in log_list:
            admin = log.admins
            resp_data.append({
                'id': log.id,
                'ip': log.ip,
                'reason': log.reason,
                'addtime': str(log.addtime),
                'admin': {
                    'id': admin.id,
                    'name': admin.name
                }
            })
        return make_response(code=0, data=resp_data, msg='Success')
