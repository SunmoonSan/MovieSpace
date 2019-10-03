#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/9 23:53
from flask_restful import Api
from app.home import home_api
from app.home.comment_views import CommentListView
from app.home.home_views import PreviewListView, MovieListView, AboutView
from app.home.movie_views import MovieView, MovieCollectView, MovieCommentView, MovieIsCollectedView
from app.home.profile_views import ProfileView, PasswordModifyView, MyMovieCollectView
from app.home.user_views import Register, Login, Logout
from app.home.index import Index

api = Api(app=home_api, prefix='/')

api.add_resource(Index, '')
api.add_resource(Register, 'register')
api.add_resource(Login, 'login')
api.add_resource(Logout, 'logout')
api.add_resource(ProfileView, 'profile')
api.add_resource(PasswordModifyView, 'password/modify')
api.add_resource(MyMovieCollectView, 'profile/moviecols')

# 首页
api.add_resource(PreviewListView, 'preview/list')
api.add_resource(MovieListView, 'movie/list')
api.add_resource(AboutView, 'about')

# Movie
api.add_resource(MovieView, 'movie/<movie_id>')
api.add_resource(MovieIsCollectedView, 'movie/<movie_id>/isCollected')
api.add_resource(MovieCommentView, 'movie/<movie_id>/comment/list')

# Comment
api.add_resource(MovieCollectView, 'movie/<movie_id>/collect')
