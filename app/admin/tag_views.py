#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/12 14:21
import datetime

from flask_restful import Resource, reqparse

from app import db
from app.models import Tag
from app.utils.response import make_response

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


class TagList(Resource):

    def get(self):
        return 'tag'

    # 添加一个新标签
    def post(self):
        args = parser.parse_args()
        name = args['name']
        print(name)
        tag = Tag.query.filter_by(name=name).first()
        if tag is None:
            db.session.add(Tag(name=name, addtime=datetime.datetime.now()))
            db.session.commit()
            return make_response(code=0)
        else:
            return make_response(code=1, msg='该标签已经存在!')
