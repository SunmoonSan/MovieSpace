#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:58
# @site  : https://github.com/SunmoonSan
from flask import Blueprint

home_api = Blueprint('home_api', __name__)

from . import urls

