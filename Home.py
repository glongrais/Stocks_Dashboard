import yfinance as yf
import streamlit as st

st.title('Portfolio Dashboard')

Total = yf.Ticker("TTE.PA")
print('bonjour')