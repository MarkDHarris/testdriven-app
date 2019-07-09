# services/users/project/__init__.py

import os
import sys
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy(app)

class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

# print(app.config, file=sys.stderr)

api.add_resource(UsersPing, '/users/ping')