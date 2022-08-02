from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models import Line, Stock, Transaction, TransactionType
import string
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

def add_stock(symbol: string, name: string, currentPrice:float, previousClose:float, sector: string, dividendYield:float, logoUrl:string):
    s = Stock(symbol=symbol, name=name, currentPrice=currentPrice, previouslose=previousClose, sector=sector, dividendYield=dividendYield, logoUrl=logoUrl)
    db.session.add(s)
    db.session.commit()

def add_line(symbol: string, price: float, quantity: int, desiredPercentage: float):
    l = Line(symbol=symbol, quantity=quantity, price=price, desiredPercentage=desiredPercentage)
    db.session.add(l)
    db.session.commit()

def add_transaction(date: datetime, type: TransactionType, symbol: string, price: float, quantity: int):
    t = Transaction(date=date, type=type, symbol=symbol, quantity=quantity, price=price)
    db.session.add(t)
    db.session.commit()