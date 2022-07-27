from importlib import resources
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import streamlit as st
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ressources/stocks_api.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@st.experimental_singleton
def db_init():
    global app, db
    db.init_app(app)
    db.create_all()

class Stock(db.Model):
    symbol = db.Column(db.String(20), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Stock %r>' % self.name