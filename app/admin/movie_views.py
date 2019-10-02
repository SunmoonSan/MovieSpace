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
                'videoLink': movie.url,
                'info': movie.info,
                'imageLink': movie.logo,
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
        video_link = params.get('videoLink')
        image_link = params.get('imageLink')
        if self._is_title_existed(title=title) is None:
            db.session.add(Movie(
                title=title,
                url=video_link,
                info=params['info'],
                logo=image_link,
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
            return make_response(code=1, msg='不能添加重复电影')

    @staticmethod
    def _is_title_existed(title):
        try:
            movie = Movie.query.filter_by(title=title).first()
            if movie:
                return movie
        except Exception as err:
            print('[error]:', err)


class MovieView(Resource):

    def put(self, movie_id):
        params = request.json
        print(params)
        title = params.get('title')
        video_link = params.get('videoLink')
        info = params.get('info')
        image_link = params.get('imageLink')
        star = params.get('star')
        play_num = params.get('playNum')
        comment_num = params.get('commentNum')
        tag_id = params.get('tagId')
        area = params.get('area')
        release_time = params.get('releaseDate')
        length = params.get('length')
        addtime = datetime.datetime.now()

        movie = self._is_id_existed(movie_id=movie_id)
        if movie is not None:
            movie.title = title
            movie.url = video_link
            movie.info = info
            movie.logo = image_link
            movie.star = star
            movie.playnum = play_num
            movie.commentnum = comment_num
            movie.area = area
            # movie.release_time = release_time
            movie.length = length
            db.session.commit()
            return make_response(code=0, msg='Success')

        return make_response(code=1, msg='该电影不存在')

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
            return Movie.query.get(movie_id)
        except Exception as err:
            print('[error]:', err)
