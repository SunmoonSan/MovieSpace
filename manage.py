#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-22 16:52
# @site  : https://github.com/SunmoonSan
from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from app import create_app
from app.config import FlaskConfig


app = create_app(FlaskConfig)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))


if __name__ == '__main__':
    manager.run()
