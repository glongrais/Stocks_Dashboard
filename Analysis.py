import yfinance as yf
import streamlit as st
import Database as db

@st.cache
def get_total_value():
    total = 0
    quantity = db.get_lines_column('quantity')

    for s in quantity:
        total += quantity[s] * db.get_stock_current_price_from_symbol(s)

    return int(total)

def get_portfolio_performance():
    total = get_total_value()
    bought = 0.0

    data = db.get_lines_columns('quantity, price')
    for i in range(len(data)):
        bought += data[i]['quantity'] * data[i]['price']
    
    return int((float(total*100)/bought)-100)