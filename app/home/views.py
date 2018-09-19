#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:59
# @site  : https://github.com/SunmoonSan
from flask import render_template, app, Blueprint

home = Blueprint('home', __name__, url_prefix='')


@home.route('/')
def index():
    return render_template('index.html')