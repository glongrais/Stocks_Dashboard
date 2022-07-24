import yfinance as yf
import streamlit as st
import File_load as fl

portfolio_path = "ressources/stocks.json"

st.title('Portfolio Dashboard')

fl.load_file(portfolio_path)

#Total = yf.Ticker("TTE.PA")

st.write(fl.json_data)