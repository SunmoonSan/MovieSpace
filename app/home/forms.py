#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:59
# @site  : https://github.com/SunmoonSan
from flask_wtf import FlaskForm
from wtforms import StringField


class RegisterForm(FlaskForm):
    name = StringField(
        label='昵称',
        render_kw={
            ''
        }
    )

