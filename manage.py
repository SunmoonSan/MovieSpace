#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-22 16:52
# @site  : https://github.com/SunmoonSan
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from app.dbs import db

migrate = Migrate(app=app,db=db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()