#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/9/11 00:16
from flask_restful import Api
from app.admin import admin_api
from app.admin.index import Index
from app.admin.movie_views import MovieListView, MovieView
from app.admin.preview_views import PreviewListView, PreviewView
from app.admin.tag_views import TagListView, TagView

api = Api(app=admin_api, prefix='/')

api.add_resource(Index, '')

# Tag类
api.add_resource(TagListView, 'tag/list')
api.add_resource(TagView, 'tag/<tag_id>')

api.add_resource(PreviewListView, 'preview/list')
api.add_resource(PreviewView, 'preview/<preview_id>')

# Movie类
api.add_resource(MovieListView, 'movie/list')
api.add_resource(MovieView, 'movie/<movie_id>')
