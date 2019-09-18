import os

from flask import Flask

# from app.config import FlaskConfig

# app = Flask(__name__)
# app.config.from_object(FlaskConfig)

# app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
# app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
from app import create_app

app = create_app(None)
if __name__ == '__main__':
    app.run()
