#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 22:16
# @site  : https://github.com/SunmoonSan
from flask import Blueprint, render_template, flash, redirect, url_for, session, request, g
from werkzeug.security import generate_password_hash

from app.admin.forms import LoginForm, TagForm, AdminForm, AuthForm, RoleForm
from app.dbs import db
from app.models import Admin, Adminlog, Tag, Oplog, Auth, Role

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
def index():
    """
    后台主页
    :return:
    """
    g.logo = 'photo2.jpg'
    return render_template('admin/index.html')


@admin.route('/login/', methods=['GET', 'POST'])
def admin_login():
    """
    后台登录
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()

        if not admin.check_pwd(data['pwd']):
            flash('密码错误', 'err')
            return redirect(url_for('admin.index'))

        session['admin'] = data['account']
        session['admin_id'] = admin.id

        adminlog = Adminlog(
            admin_id=admin.id,
            ip=request.remote_addr
        )

        db.session.add(adminlog)
        db.session.commit()
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route('/auth/add/', methods=['GET', 'POST'])
def auth_add():
    """
    添加权限
    :return:
    """
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth = Auth(
            name=data['name'],
            url=data['url']
        )
        db.session.add(auth)
        db.session.commit()
        flash('添加权限成功!', 'ok')
    return render_template('admin/auth_add.html', form=form)


@admin.route('/auth/list/<int:page>/', methods=['GET'])
@admin.route('/auth/list/', methods=['GET'])
def auth_list(page=None):
    """
    权限列表
    :return:
    """
    print(page)
    if page is None:
        page = 1

    page_data = Auth.query.order_by(
        Auth.addtime.desc()
    ).paginate(page=page, per_page=2)

    return render_template('admin/auth_list.html', page_data=page_data)


@admin.route('/auth/del/<int:id>/', methods=['GET'])
def auth_del(id=None):
    """
    删除权限
    :param id:
    :return:
    """
    auth = Auth.query.filter_by(id=id).first_or_404()
    db.session.delete(auth)
    db.session.commit()
    flash('删除权限成功!', 'ok')
    return redirect(url_for('admin.auth_list', page=1))


@admin.route('/auth/edit/<int:id>', methods=['GET', 'POST'])
def auth_edit(id=None):
    """
    编辑权限
    :param id:
    :return:
    """
    form = AuthForm()
    auth = Auth.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        auth.url = data['url']
        auth.name = data['name']
        db.session.add(auth)
        db.session.commit()
        flash('权限修改成功!', 'ok')
        redirect(url_for('admin.auth_edit', id=id))
    return render_template('admin/auth_edit.html', form=form, auth=auth)


@admin.route('/role/add/', methods=['GET', 'POST'])
def role_add():
    """
    角色添加
    :return:
    """
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        role = Role(
            name=data['name'],
            auths=','.join(map(lambda v: str(v), data['auths']))
        )
        db.session.add(role)
        db.session.commit()
        flash('添加角色成功!', 'ok')
    return render_template('admin/role_add.html', form=form)


@admin.route('/role/list/<int:page>/', methods=['GET'])
def role_list(page=None):
    """
    角色列表
    :param page:
    :return:
    """
    if page is None:
        page = 1
    page_data = Role.query.order_by(
        Role.addtime.desc()
    ).paginate(page=page, per_page=2)
    return render_template('admin/role_list.html', page_data=page_data)


@admin.route('/role/del/<int:id>/', methods=['GET'])
def role_del(id=None):
    """
    删除角色
    :param id:
    :return:
    """
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    flash('删除角色成功!', 'ok')
    return redirect(url_for('admin.role_list', page=1))


@admin.route('/role/edit/<int:id>/', methods=['GET', 'POST'])
def role_edit(id=None):
    """
    编辑角色
    :param id:
    :return:
    """
    form = RoleForm()
    role = Role.query.get_or_404(id)
    if request.method == 'GET':
        auths = role.auths
        form.auths.data = list(map(lambda v: int(v), auths.split(',')))
    if form.validate_on_submit():
        data = form.data
        role.name = data['name']
        role.auths = ','.join(map(lambda v: str(v), data['auths']))
        db.session.add(role)
        db.session.commit()
        flash('修改角色成功!', 'ok')
    return render_template('admin/role_edit.html', form=form, role=role)


@admin.route('/tag/add/', methods=['GET', 'POST'])
def tag_add():
    """
    添加标签
    :return:
    """
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data['name']).count()
        if tag == 1:
            flash("标签已经存在", 'err')
            return redirect(url_for('admin.tag_add'))

        tag = Tag(name=data['name'])
        db.session.add(tag)
        db.session.commit()

        oplog = Oplog(
            admin_id=session['admin_id'],
            ip=request.remote_addr,
            reason='添加标签%s' % data['name']
        )
        db.session.add(oplog)
        db.session.commit()
        flash("标签添加成功", 'ok')
        redirect(url_for('tag_add'))

    return render_template('admin/tag_add.html', form=form)


@admin.route('/admin/add/', methods=['GET', 'POST'])
def admin_add():
    """
    添加管理员
    :return:
    """
    form = AdminForm()
    print(form)
    if form.validate_on_submit():
        data = form.data
        admin = Admin(
            name=data['name'],
            pwd=generate_password_hash(data['pwd']),
            role_id=data['role_id'],
            is_super=1
        )

        db.session.add(admin)
        db.session.commit()
        flash("添加管理员成功!", 'ok')
    return render_template('admin/admin_add.html', form=form)
