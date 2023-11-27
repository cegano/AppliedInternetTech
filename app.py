from flask import Flask, render_template, request, redirect, flash, url_for
from models import *

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Postgresql@localhost:5432/library"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/index", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        aid = request.form.get('author_id')
        author = Authors.query.get(aid)
        return render_template("findAuthor.html", author=author)

@app.route("/findBooks", methods = ["GET", "POST"])
def findBooks():
    books = Books.query.all()
    return render_template("findBooks.html", books=books)

@app.route("/showBook")
def showBook():
    bid = request.args.get('bid')
    book = Books.query.get(bid)
    return render_template("titleForm.html", book=book)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_error.html', title='error'), 404

if __name__ == "__main__":
    db.create_all()
