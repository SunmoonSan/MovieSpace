#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:59
# @site  : https://github.com/SunmoonSan
from flask import render_template, app, Blueprint

home = Blueprint('home', __name__, url_prefix='')


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/login/')
def login():
    return render_template('home/login.html')


@home.route('/logout/')
def logout():
    return render_template('home/logout.html')


@home.route('/register/')
def register():
    return render_template('home/register.html')


@home.route('/user/')
def user():
    return render_template('home/user.html')


@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')


@home.route('/comments/')
def comments():
    return render_template('home/comments.html')


@home.route('/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')


@home.route('/movielog/')
def moviecol():
    return render_template('home/moviecol.html')


@home.route('/animation/')
def animation():
    return render_template('home/animation.html')


@home.route('/search/')
def search():
    return render_template('home/search.html')