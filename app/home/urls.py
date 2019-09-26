#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/9 23:53
from flask_restful import Api
from app.home import home_api
from app.home.home_views import PreviewListView, MovieListView, AboutView
from app.home.movie_views import MovieView
from app.home.user_views import Register, Login, Logout
from app.home.index import Index

api = Api(app=home_api, prefix='/')

api.add_resource(Index, '')
api.add_resource(Register, 'register')
api.add_resource(Login, 'login')
api.add_resource(Logout, 'logout')

# 首页
api.add_resource(PreviewListView, 'preview/list')
api.add_resource(MovieListView, 'movie/list')
api.add_resource(AboutView, 'about')

# Movie
api.add_resource(MovieView, 'movie/<movie_id>')
