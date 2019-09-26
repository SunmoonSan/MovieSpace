#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/25 22:22
from flask_restful import Api
from app.auth import auth_api
from app.auth.qiniu_views import QiniuToken

api = Api(app=auth_api, prefix='/auth/')

api.add_resource(QiniuToken, 'qiniu')
