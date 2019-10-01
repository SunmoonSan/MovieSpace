#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/26 23:27
from flask import request
from flask_restful import Resource

from app import db
from app.auth.auth_views import Auth
from app.models import Movie, Moviecol
from app.utils.response import make_response


class MovieView(Resource):
    """根据ID获取电影"""

    def get(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is not None:
            return make_response(
                code=0, data={
                    'id': movie.id,
                    'title': movie.title,
                    'imageLink': movie.logo,
                    'videoLink': movie.url,
                    'length': movie.length,
                    'area': movie.area,
                    'releaseTime': movie.release_time,
                    'info': movie.info,
                },
                msg='Success')
        return make_response(code=1, msg='该电影不存在!')


class MovieCollectView(Resource):

    def post(self, movie_id):
        resp = Auth.identify(request.headers)
        if not resp['allow_access']:
            return make_response(code=1, msg=resp['msg'])

        user_id = resp['user_id']

        try:
            db.session.add(Moviecol(movie_id=movie_id, user_id=user_id))
            db.session.commit()
            return make_response(code=0, msg='Success')
        except Exception as  err:
            return make_response(code=1, msg=str(err))
