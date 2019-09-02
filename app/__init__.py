#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 15:31
# @site  : https://github.com/SunmoonSan
from app.app import app
from app.home import home
from app.admin import admin

app.register_blueprint(home)
app.register_blueprint(admin)



