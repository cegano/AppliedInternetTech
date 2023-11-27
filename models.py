from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Authors(db.Model):
    __tablename__ = "authors"
    aid = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    year_born = db.Column(db.Integer, nullable=False)
    books = db.relationship("Books", backref="authors")

class Books(db.Model):
    __tablename__ = "books"
    bid = db.Column(db.Integer, primary_key=True)
    aid = db.Column(db.Integer, db.ForeignKey('authors.aid'), nullable=False)
    title = db.Column(db.String, nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
