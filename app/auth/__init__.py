#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/25 22:21
from flask import Blueprint

auth_api = Blueprint('auth_api', __name__)

from . import urls