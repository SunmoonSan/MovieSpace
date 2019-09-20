#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/18 16:21
import datetime
import os

from flask import request, current_app
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app import db
from app.models import Preview
from app.utils.response import make_response


class PreviewListView(Resource):

    # 获取预告列表
    def get(self):
        preview_list = Preview.query.all()
        resp_data = []
        for preview in preview_list:
            resp_data.append({
                'id': preview.id,
                'title': preview.title,
                'url': preview.logo,
                'addtime': str(preview.addtime)
            })
        return make_response(code=0, data=resp_data, msg='Success')

    # 新建预告
    def post(self):
        title = request.form['title']
        preview_img = request.files['previewImg']
        preview = Preview.query.filter_by(title=title).first()
        if preview is None:
            if preview_img and self.allowed_file(preview_img.filename):
                filename = secure_filename(preview_img.filename)
                preview_img.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

                if os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], filename)):
                    db.session.add(
                        Preview(title=title, logo=os.path.join(current_app.config['UPLOAD_FOLDER'], filename),
                                addtime=datetime.datetime.now()))
                    db.session.commit()
                    return make_response(code=0, msg='Success')
            else:
                return make_response(code=1, msg='文件格式不正确!')
        else:
            return make_response(code=1, msg='该标签已经存在!')

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']


class PreviewView(Resource):

    def put(self, preview_id):
        preview = self._is_id_existed(preview_id=preview_id)
        if preview is not None:
            db.session.delete(preview)
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该预告不存在!')

    def delete(self, preview_id):
        preview = self._is_id_existed(preview_id=preview_id)
        if preview is not None:
            db.session.delete(preview)
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该预告不存在!')

    @staticmethod
    def _is_id_existed(preview_id):
        try:
            preview = Preview.query.get_or_404(preview_id)
            if preview:
                return preview
        except Exception as err:
            print('[error]:', err)
