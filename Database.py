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

def get_stocks_symbol_list():
    query = f'SELECT symbol FROM Line'
    response = db.session.execute(query)
    values = response.fetchall()
    result = [v['symbol'] for v in values]
    return result

def get_stocks_column(column):
    query = f'SELECT '+column+' FROM Stock'
    response = db.session.execute(query)
    result = response.fetchall()
    return result