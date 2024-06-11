from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Product %r>' % self.name


class Rider(db.Model):
    __tablename__ = "riders"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

    def __repr__(self):
        return '<Rider %r>' % self.name
