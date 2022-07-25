import yfinance as yf
import streamlit as st
import File_load as fl
import Analysis as an
import API_call as ac

portfolio_path = "ressources/stocks.json"

st.title('Portfolio Dashboard')

fl.load_file(portfolio_path)

stocks_list = []
quantity = {}
pru = {}

for s in fl.json_data:
    stocks_list.append(s['symbol'])
    quantity[s['symbol']] = int(s['quantity'])
    pru[s['symbol']] = float(s['price'])

ac.load_data(" ".join(stocks_list))

total_value = an.get_total_value(ac.get_raw_data().tickers, quantity)
protfolio_performance = an.get_portfolio_performance(ac.get_raw_data().tickers, quantity, pru)

st.metric("Total amount", str(total_value)+"€", delta=str(protfolio_performance)+"%")