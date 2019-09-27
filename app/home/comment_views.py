#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/27 01:12
import datetime

from flask import request, g, session
from flask_restful import Resource

from app import db
from app.models import Comment


class CommentView(Resource):

    def post(self, movie_id):
        params = request.json
        content = params['content']

        print(session)
        # db.session.add(Comment(
        #     content=content,
        #     addtime=datetime.datetime.now(),
        #     movie_id=movie_id,
        #     user_id=session['user_id']
        # ))
        print(session)
        return 'comment'
