#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/21 09:58
import datetime

from flask import request
from flask_restful import Resource

from app import db
from app.models import Movie
from app.utils.response import make_response


class MovieListView(Resource):

    def get(self):
        movie_list = Movie.query.all()
        resp_data = []
        for movie in movie_list:
            resp_data.append({
                'id': movie.id,
                'title': movie.title,
                'url': movie.url,
                'info': movie.info,
                'logoLink': movie.logo,
                'star': movie.star,
                'playNum': movie.playnum,
                'commentNum': movie.commentnum,
                'tagId': movie.tag_id,
                'area': movie.area,
                'releaseTime': movie.release_time,
                'length': movie.length,
                'addtime': str(movie.addtime)
            })
        return make_response(code=0, data=resp_data, msg='Success')

    def post(self):
        params = request.json
        title = params.get('title')
        url = params.get('videoLink')
        logo_link = params.get('logoLink')
        if self._is_title_existed(title=title) is None:
            db.session.add(Movie(
                title=title,
                url=url,
                info=params['info'],
                logo=params['logoLink'],
                # star=params['star'],
                # playnum=params['playNum'],
                # commentnum=params['commentNum'],
                # tag_id=params['tagId'],
                area=params['area'],
                # release_time=params['releaseDate'],
                length=params['length'],
                addtime=datetime.datetime.now()))
            db.session.commit()
            return make_response(code=0)
        else:
            return make_response(code=1, msg='不能添加重复预告')

    @staticmethod
    def _is_title_existed(title):
        try:
            movie = Movie.query.filter_by(title=title).first()
            if movie:
                return movie
        except Exception as err:
            print('[error]:', err)


class MovieView(Resource):

    def put(self):
        pass

    def delete(self, movie_id):
        movie = self._is_id_existed(movie_id=movie_id)
        if movie is not None:
            db.session.delete(movie)
            db.session.commit()
            return make_response(code=0, msg='Success')
        else:
            return make_response(code=1, msg='该电影不存在!')

    @staticmethod
    def _is_id_existed(movie_id):
        try:
            movie = Movie.query.get_or_404(movie_id)
            if movie:
                return movie
        except Exception as err:
            print('[error]:', err)

