#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-21 15:31
# @site  : https://github.com/SunmoonSan
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from qiniu import Auth
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config=None):
    app = Flask(__name__, static_folder='app/static/')
    CORS(app=app)
    if config is not None:
        app.config.from_object(config)

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    login_manager.init_app(app)

    # 配置原生SQL执行
    engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/movie", max_overflow=0, pool_size=5)
    Session = sessionmaker(bind=engine)
    session = Session()
    app.config['session'] = session

    # 七牛云
    qiniu = Auth("ux4DxWb-TJNjReQH6Nms_fPADLkBh4P4dIfg3dgY", "D5FenVgla1hB7cZbAXUCa3M_V_St7-SR8DKN0AUb")
    app.config['qiniu'] = qiniu

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.get(user_id)

    from app.home import home_api
    app.register_blueprint(home_api)

    from app.admin import admin_api
    app.register_blueprint(admin_api, url_prefix='/admin')

    from app.auth import auth_api
    app.register_blueprint(auth_api)

    return app
