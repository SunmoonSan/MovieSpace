#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/26 23:27
from flask_restful import Resource

from app.models import Movie
from app.utils.response import make_response


class MovieView(Resource):
    """根据ID获取电影"""

    def get(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is not None:
            return make_response(
                code=0, data={
                    'id': movie.id,
                    'title':movie.title,
                    'imageLink': movie.logo,
                    'videoLink': movie.url,
                    'info': movie.info,
                },
                msg='Success')
        return make_response(code=1, msg='该电影不存在!')