#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 15:31
# @site  : https://github.com/SunmoonSan
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# from app.home import home
# from app.admin import admin

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    from app.home import home
    app.register_blueprint(home)

    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
