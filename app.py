from flask import Flask, render_template, request
from models import *
app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] ="postgresql://postgres:Postgresql@localhost:5432/CIT109"
app.config ["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def index():
    stu = ruby_on_rails.query.all()
    return render_template("index.html", stu=stu, heading='Students Data')

@app.route("/major", methods=['GET', 'POST'])
def by_major():
    if request.method=='GET':
        return render_template("majorForm.html")
    else:
        major = request.form.get('major')
        stu = ruby_on_rails.query.filter_by(major=major).all()
        return render_template("index.html", stu=stu, heading='Students by Major')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_not_found.html'), 404

if __name__ == "__main__":
    db.create_all()
