from datetime import datetime

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)
    published = db.Column(db.Boolean(), default=False)

    # created_by = db.relationship('User', backref='posts')
    # author_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False, default=1)


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)


class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    _password = db.Column(db.String(), nullable=False)

    # posts = db.relationship('Post', backref='created_by', lazy=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, text):
        self.password = generate_password_hash(text)

    def check_password(self, text):
        return check_password_hash(self.password, text)


