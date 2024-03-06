from flask import Flask
from os import path
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
#from web_service.config import Config


def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'nnevo0inerv32'
    app.config['UPLOAD_FOLDER'] = 'static/files'
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    return app