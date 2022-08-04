import yfinance as yf
import streamlit as st
from Database_operations import add_stock

@st.cache
def load_data(stock_list):
    tickers = yf.Tickers(stock_list)

    for t in tickers.tickers.values():
        stock = t.info
