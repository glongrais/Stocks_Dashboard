import json as js
import streamlit as st
from Database_operations import add_line

@st.experimental_singleton
def load_file(name):
    f = open(name)
    json_data = js.load(f)
    for s in json_data:
        add_line(symbol=s['symbol'], quantity=int(s['quantity']),price=float(s['price']),desiredPercentage=float(s['desired_percentage']))
    
    return json_data