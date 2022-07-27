import enum
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
    db.drop_all()
    db.create_all()

class Stock(db.Model):
    symbol = db.Column(db.String(20), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    sector = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Stock %r>' % self.name

class Line(db.Model):
    symbol = db.Column(db.String(20), nullable=False, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    desired_percent = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Line %r>' % self.symbol

class TransactionType(enum.Enum):
    SELL = "SELL"
    BUY = "BUY"
    DIVIDEND = "DIVIDEND"

class Transaction(db.Model):
    id = db.Column(db.integer, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    symbol = db.Column(db.String(50), nullable=False)
    type = db.Coluumn(db.Enum(TransactionType), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Line %r>' % self.symbol