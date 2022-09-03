import yfinance as yf
import streamlit as st
import File_load as fl
import Analysis as an
import API_call as ac
import Database as db

from Models import Stock

def button_call():
    Stock.__table__.drop()
    Stock.__table__.create(db.session.bind, checkfirst=True)
    st.legacy_caching.clear_cache()

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

st.sidebar.button('Refresh', on_click=button_call)