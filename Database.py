from unittest import result
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import streamlit as st
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ressources/stocks_api.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def row2dict(rows, column):
    d = {}

    for r in rows:
        d[r['symbol']] = r[column]

    return d

@st.experimental_singleton
def db_init():
    global app, db
    db.init_app(app)
    db.drop_all()
    db.create_all()

def get_stocks_symbol_list():
    query = f'SELECT symbol FROM Line'
    response = db.session.execute(query)
    values = response.fetchall()
    result = [v['symbol'] for v in values]
    return result

def get_lines_column(column):
    query = f'SELECT '+column+',symbol FROM Line'
    response = db.session.execute(query)
    result = response.fetchall()
    return row2dict(result, column)

def get_lines_columns(column):
    query = f'SELECT '+column+',symbol FROM Line'
    response = db.session.execute(query)
    result = response.fetchall()
    return result

def get_stocks_columns(column):
    query = f'SELECT '+column+',symbol FROM Stock'
    response = db.session.execute(query)
    result = response.fetchall()
    return result

def get_stock_current_price_from_symbol(symbol):
    query = f'SELECT currentPrice FROM Stock WHERE symbol=\''+symbol+'\''
    response = db.session.execute(query)
    value = response.fetchall()
    result = 0
    if len(value) > 0:
        result = value[0]['currentPrice']
    return result

def get_stock_field_from_symbol(field, symbol):
    query = f'SELECT '+field+' FROM Stock WHERE symbol=\''+symbol+'\''
    response = db.session.execute(query)
    value = response.fetchall()
    result = 0
    if len(value) > 0:
        result = value[0][field]
    return result

