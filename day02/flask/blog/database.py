from flask_pymongo import PyMongo
from flask import Flask

mongo = PyMongo()


def configure(app: Flask):
    mongo.init_app(app)
