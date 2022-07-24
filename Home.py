import yfinance as yf
import streamlit as st
import File_load as fl
import Analysis as an

portfolio_path = "ressources/stocks.json"

st.title('Portfolio Dashboard')

fl.load_file(portfolio_path)

tot = an.get_total_value(fl.json_data)

st.metric("Total amount", str(tot)+"€")
