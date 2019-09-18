#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-22 14:19
# @site  : https://github.com/SunmoonSan


class FlaskConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/movie"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "sansansan"
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'sql']
