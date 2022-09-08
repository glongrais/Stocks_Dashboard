import yfinance as yf
import streamlit as st
import File_load as fl
import Analysis as an
import API_call as ac
import Database as db

from Models import Stock

import pandas as pd
import numpy as np

def button_call():
    Stock.__table__.drop(db.db.engine)
    Stock.__table__.create(db.db.session.bind, checkfirst=True)
    st.legacy_caching.clear_cache()

def edit_goal_dividend():
    st.session_state['dividend_goal'] = 10000

portfolio_path = "ressources/stocks.json"

st.title('Portfolio Dashboard')

db.db_init()

json_data = fl.load_file(portfolio_path)

stocks_list = db.get_stocks_symbol_list()

quantity = {}
pru = {}

for s in json_data:
    quantity[s['symbol']] = int(s['quantity'])
    pru[s['symbol']] = float(s['price'])

ac.load_data(stocks_list)
total_value = an.get_total_value()
total_dividend_amount = an.get_yearly_dividend_amount()
total_dividend_percentage = an.get_yearly_dividend_percentage()

protfolio_performance = an.get_portfolio_performance()

col1, col2, col3 = st.columns(3)

col1.metric("Total amount", str(total_value)+"€", delta=str(protfolio_performance)+"%")
col2.metric("Dividend €", str(total_dividend_amount)+"€")
col3.metric("Dividend %", str(total_dividend_percentage)+"%")

if 'dividend_goal' not in st.session_state:
    st.session_state['dividend_goal'] = 50000
col4, col5, col6, col7 = st.columns(4)

col4.write("Dividend goal : ")
col5.progress(int(round(total_dividend_amount*100/st.session_state['dividend_goal'],0)))
col6.write(str(int(round(total_dividend_amount*100/st.session_state['dividend_goal'],0))) + " \% of "+str(st.session_state['dividend_goal'])+"€ / year")
b1 = col7.button(label="Edit goal", on_click=edit_goal_dividend)


col4, col5, col6, col8 = st.columns(4)

col4.write("Portfolio goal :")
col5.progress(int(round(total_value*100/500000,0)))
col6.write(str(int(round(total_value*100/500000,0))) + " \% of 500 000 € ")
b2 = col8.button(label="Edit goal")

st.sidebar.button('Refresh', on_click=button_call)