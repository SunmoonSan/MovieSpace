#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/11 00:16
from flask_restful import Api
from app.admin import admin_api
from app.admin.index import Index
from app.admin.tag_views import TagList

api = Api(app=admin_api, prefix='/')

api.add_resource(Index, '')

# Tag类
api.add_resource(TagList, 'tag/list')
