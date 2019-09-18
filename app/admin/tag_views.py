#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/12 14:21
import datetime

from flask import request
from flask_restful import Resource, reqparse, abort
from pymysql import IntegrityError

from app import db
from app.models import Tag
from app.utils.response import make_response

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


class TagList(Resource):

    def get(self):
        tag_list = Tag.query.all()
        resp_data = []
        for tag in tag_list:
            resp_data.append({
                'id': tag.id,
                'name': tag.name,
                'addtime': str(tag.addtime)
            })
        return make_response(code=0, data=resp_data, msg='Success')

    # 添加一个新标签
    def post(self):
        args = parser.parse_args()
        name = args['name']
        tag = Tag.query.filter_by(name=name).first()
        if tag is None:
            db.session.add(Tag(name=name, addtime=datetime.datetime.now()))
            db.session.commit()
            return make_response(code=0)
        else:
            return make_response(code=1, msg='该标签已经存在!')


class TagOp(Resource):

    def get(self, tag_id):
        return tag_id

    def put(self, tag_id):
        params = request.json
        resp_data = {}
        try:
            db.session.query(Tag).filter_by(id=tag_id).update({'name': params['name']})
            db.session.commit()
            resp_data.update({
                'code': 0,
                'msg': 'Success'
            })
        except Exception as err:
            print('[error]:', err)
            resp_data.update({
                'code': 1,
                'msg': str(err)
            })
        finally:
            db.session.close()
        return make_response(code=resp_data['code'], msg=resp_data['msg'])

    def delete(self, tag_id):
        tag = self._is_existed(tag_id)
        if tag is not None:
            db.session.delete(tag)
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg="该标签不存在!")

    @staticmethod
    def _is_existed(tag_id):
        try:
            tag = Tag.query.get(tag_id)
            if tag:
                return tag
        except Exception as err:
            print('[error]:', err)
