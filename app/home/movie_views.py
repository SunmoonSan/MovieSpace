#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/26 23:27
import datetime
from operator import and_

from flask import request
from flask_restful import Resource

from app import db
from app.auth.auth_views import Auth
from app.models import Movie, Moviecol, Comment, User
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


class MovieCommentView(Resource):

    def get(self, movie_id):
        """
        更加电影ID获取该电影下的评论list
        :param movie_id: 电影ID
        :return:
        """
        comment_list = Comment.query.join(User).filter(
            and_(User.id == Comment.user_id, Comment.movie_id == movie_id)).order_by(
            Comment.addtime.desc()).all()
        resp_data = []
        for comment in comment_list:
            user = comment.users
            resp_data.append({
                'id': comment.id,
                'content': comment.content,
                'addtime': str(comment.addtime),
                'commentUser': {
                    'id': user.id,
                    'name': user.name,
                    'avatar': user.face
                }
            })
        return make_response(code=0, data=resp_data, msg='Success')

    def post(self, movie_id):
        """
        根据电影ID为该电影新建一条评论
        :param movie_id:
        :return:
        """
        resp = Auth.identify(request.headers)
        if not resp['allow_access']:
            return make_response(code=1, msg=resp['msg'])
        user_id = resp['user_id']

        params = request.json
        content = params['content']

        db.session.add(Comment(
            content=content,
            addtime=datetime.datetime.now(),
            movie_id=movie_id,
            user_id=user_id
        ))
        db.session.commit()
        return make_response(code=0, msg='Success')


class MovieCollectView(Resource):
    """收藏/取消收藏电影"""

    def post(self, movie_id):
        resp = Auth.identify(request.headers)
        if not resp['allow_access']:
            return make_response(code=1, msg=resp['msg'])

        user_id = resp['user_id']

        moviecol = Moviecol.query.filter(and_(Moviecol.movie_id == movie_id, Moviecol.user_id == user_id)).first()
        if moviecol is None:
            db.session.add(Moviecol(movie_id=movie_id, user_id=user_id))
            db.session.commit()
        else:
            db.session.delete(moviecol)
            db.session.commit()
        return make_response(code=0, msg='Success')


class MovieIsCollectedView(Resource):
    """根据电影ID判断是否已经被当前用户收藏"""

    def get(self, movie_id):
        resp = Auth.identify(request.headers)
        if not resp['allow_access']:
            return make_response(code=1, msg=resp['msg'])

        user_id = resp['user_id']
        count = Moviecol.query.filter(and_(Moviecol.movie_id == movie_id, Moviecol.user_id == user_id)).count()
        return make_response(code=0, data={'isCollected': count > 0}, msg='Success')
