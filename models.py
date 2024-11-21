from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from flask import current_app
from authlib.jose import jwt
import time

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_in=1800):
        header = {'alg': 'HS256'}
        key = current_app.config['SECRET_KEY']
        data = {'user_id': self.id, 'exp': time.time() + expires_in}
        token = jwt.encode(header, data, key)
        return token.decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        key = current_app.config['SECRET_KEY']
        try:
            data = jwt.decode(token, key)
            if data['exp'] < time.time():
                return None
            user_id = data['user_id']
        except:
            return None
        return User.query.get(user_id)

class Searches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('searches', lazy=True))
    item = db.Column(db.String(120), nullable=False)
    date_search = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)