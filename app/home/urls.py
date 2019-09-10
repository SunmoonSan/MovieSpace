#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/9 23:53
from flask_restful import Api

from app.home import home_api
from app.home.auth import Register
from app.home.index import Index

api = Api(app=home_api, prefix='/')

api.add_resource(Index, '')
api.add_resource(Register, 'register')