from flask import Flask, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)

@app.route("/")
def index():
    posts = mongo.db.posts.find()
    
    content_url = url_for("read_content", slug="qualquer-coisa")
    return (
        f"<h1>Boas vindas a {app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Leia um post</a>"
        "<hr>"
        f"{request.args.get('author')}"  # NEW
        f"{list(posts)}"
    )

@app.errorhandler(404)
def not_found_page(error):
    return f"Not found page {app.config['APP_NAME']}"


def read_content(slug):
    index_url = url_for("index")
    return f"<h1>{slug}</h1><a href='{index_url}'>Voltar ao inicio</a>"

app.add_url_rule("/<string:slug>", view_func=read_content)
