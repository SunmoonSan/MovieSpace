#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:59
# @site  : https://github.com/SunmoonSan
import uuid

from flask import render_template, app, Blueprint, flash, redirect, url_for, session, request

from app.admin.forms import RegisterForm, LoginForm
from app.dbs import db
from app.models import Tag, User, Userlog

home = Blueprint('home', __name__, url_prefix='')


@home.route('/')
def index():
    tags = Tag.query.all()

    return render_template('home/index.html',
                           tags=tags)


@home.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        data = form.data
        user = User.query.filter_by(name=data['name']).first()
        if user:
            if not user.check_pwd(data['pwd']):
                flash('密码错误!', 'error')
                return redirect(url_for('login'))
        else:
            flash('账户不存在!', 'error')
            return redirect(url_for('home.login'))

        session['user'] = user.name
        session['id'] = user.id

        userlog = Userlog(
            user_id=user.id,
            ip = request.remote_addr
        )
        db.session.add(userlog)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('home/login.html', form=form)


@home.route('/logout/')
def logout():
    return render_template('home/logout.html')


@home.route('/register/', methods=['GET', 'POST'])
def register():
    """
    用户注册
    :return:
    """
    form = RegisterForm()
    if form.is_submitted():
        data = form.data
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            pwd=data['password'],
            uuid=uuid.uuid4().hex
        )

        db.session.add(user)
        db.session.commit()
        flash('注册成功!', 'ok')

    return render_template('home/register.html', form=form)


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
