#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-09-19 06:59
# @site  : https://github.com/SunmoonSan
import uuid

from flask import render_template, app, Blueprint, flash, redirect, url_for, session, request
from werkzeug.security import generate_password_hash

from app.home.forms import RegisterForm, LoginForm, UserProfileForm, PasswordForm
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
    if form.validate_on_submit():
        data = form.data
        print(data)
        user = User.query.filter_by(name=data['name']).first()
        if user:
            if not user.check_pwd(data['pwd']):
                flash('密码错误!', 'error')
                return redirect(url_for('home.login'))
        else:
            flash('账户不存在!', 'error')
            return redirect(url_for('home.login'))

        session['user'] = user.name
        session['id'] = user.id

        userlog = Userlog(
            user_id=user.id,
            ip=request.remote_addr
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
            pwd=generate_password_hash(data['pwd']),
            uuid=uuid.uuid4().hex
        )

        db.session.add(user)
        db.session.commit()
        flash('注册成功!', 'ok')

    return render_template('home/register.html', form=form)


@home.route('/user/', methods=['GET', 'POST'])
def user():
    form = UserProfileForm()
    user_id = session['id']
    user = User.query.filter_by(id=user_id).first()
    print(user)
    if form.validate_on_submit():
        data = form.data

        user.name = data['name']
        user.email = data['email']
        user.phone = data['phone']
        user.info = data['info']

        db.session.add(user)
        db.session.commit()
        flash('用户信息更新成功!', 'ok')
        return redirect(url_for('home.user'))
    return render_template('home/user.html', form=form, user=user)


@home.route('/pwd/', methods=['GET', 'POST'])
def pwd():
    form = PasswordForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template('home/pwd.html', form=form)


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
