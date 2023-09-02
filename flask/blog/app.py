from flask import Flask, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)
