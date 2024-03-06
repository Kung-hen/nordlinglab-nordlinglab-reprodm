import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    UPLOAD_FOLDER = config.get('UPLOAD_FOLDER')
