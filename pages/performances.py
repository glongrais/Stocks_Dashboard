import streamlit as st
import Database as db
import pandas as pd
import Analysis as an

st.title("Performances")

lines_data = db.get_lines_columns("quantity, price")
stocks_data = db.get_stocks_columns("currentPrice, name, previousClose")

df1 = pd.DataFrame(lines_data, columns =  ["Quantity", "Price", "Symbol"])
df2 =pd.DataFrame(stocks_data, columns =  ["Current Price", "Name", "Previous Close","Symbol"])
df2 = df2.assign(priceVariation = df2["Current Price"] - df2["Previous Close"]).drop('Previous Close', 1).rename(columns={"priceVariation":"Price Variation"})

total_value = an.get_total_value()

df = pd.merge(df1, df2, on=["Symbol"])

#df = df[["Symbol", "Name", "Quantity", "Price", "Current Price", "priceVariation"]]

st.table(df)