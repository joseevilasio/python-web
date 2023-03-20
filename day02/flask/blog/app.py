from flask import Flask, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)


app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = PyMongo(app)


# Adicionamos um error handler
@app.errorhandler(404)
def not_found_page(error):
    return f"<strong>Desculpe</strong> página não encontrada em {app.config['APP_NAME']}"
                

@app.route("/")
def index():
    posts = mongo.db.posts.find()  # NEW
    content_url = url_for("read_content", slug="qualquer-coisa")
    return (
        f"<h1>Boas vindas a {app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Leia um post</a>"
        "<hr>"       
        f"{list(posts)}"  # NEW
    )


def read_content(slug):
    index_url = url_for("index")
    return f"<h1>{slug}</h1><a href='{index_url}'>Voltar ao inicio</a>"

app.add_url_rule("/<string:slug>", view_func=read_content)
