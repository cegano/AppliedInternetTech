from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ruby_on_rails(db.Model):
    __tablename__ = "ruby_on_rails"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    hrs_attempted = db.Column(db.Integer, nullable=False)
    gpa_points = db.Column(db.Float, nullable=False)
    major = db.Column(db.String, nullable=False)
