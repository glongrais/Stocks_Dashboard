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