#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/25 22:21
from flask import current_app
from flask_restful import Resource
from qiniu import Auth

from app.utils.response import make_response


class QiniuToken(Resource):

    def get(self):
        qiniu = current_app.config['qiniu']
        token = qiniu.upload_token(bucket='moviespace001', expires=3600)
        return make_response(code=0, data={'token': token}, msg='Success')