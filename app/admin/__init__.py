#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 22:15
# @site  : https://github.com/SunmoonSan
from flask import Blueprint

admin_api = Blueprint('admin_api', __name__)

from . import urls
