import yfinance as yf
import streamlit as st
import threading
from Database_operations import add_stock

@st.cache(suppress_st_warning=True)
def load_data(stock_list):

    threads = []

    for s in stock_list:
        t = threading.Thread(target=load_one_stock, args=(s,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()


def load_one_stock(symbol):
    stock = yf.Ticker(symbol).info
    if stock['quoteType'] == "EQUITY":
        add_stock(symbol=stock['symbol'], name=stock['shortName'], currentPrice=stock['currentPrice'], previousClose=stock['previousClose'], sector=stock['sector'], dividendYield=stock['dividendYield'], logoUrl=stock['logo_url'])
    elif stock['quoteType'] == "ETF":
        add_stock(symbol=stock['symbol'], name=stock['shortName'], currentPrice=stock['regularMarketPrice'], previousClose=stock['previousClose'], sector="ETF", dividendYield=0, logoUrl=stock['logo_url'])

