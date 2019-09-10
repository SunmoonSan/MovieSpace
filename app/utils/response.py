#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/10 18:53
from flask import jsonify


def make_response(code=0, data=None, msg='Success'):
    """
    构造返回的JSON数据
    :param code: 状态码
    :param data: 数据
    :param msg: 返回描述信息
    :return:
    """
    resp_data = {'code': code, 'msg': msg}
    if data is not None:
        resp_data.update({'data': data})
    return jsonify(resp_data)
