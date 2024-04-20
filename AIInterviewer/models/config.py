# -*- coding=utf-8 -*-
import os
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @staticmethod
    def init_app(AIInterviewer):
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mongodb://root:root@127.0.0.1:27017/test'
    DEBUG = True

# define the config
config = {
    'default': DevelopmentConfig
}
