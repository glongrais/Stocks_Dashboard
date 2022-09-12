import streamlit as st
import Database as db
import pandas as pd
import Analysis as an

st.title("Estimator")

value = st.number_input("Amount to invest")

lines_data = db.get_lines_columns("quantity, desiredPercentage")
stocks_data = db.get_stocks_columns("currentPrice, name")

df1 = pd.DataFrame(lines_data, columns =  ["Quantity", "Desired Percentage", "Symbol"])
df2 =pd.DataFrame(stocks_data, columns =  ["Current Price", "Name", "Symbol"])

total_value = an.get_total_value()
to_compute = total_value + value

stocks_data = db.row2dict(stocks_data, "currentPrice")

percentages = {}

count = 0
for l in lines_data:
    price = stocks_data[l["symbol"]]*l["quantity"]
    percentage = round(price*100/to_compute,2)
    percentages[count] = (l["symbol"],percentage)
    count += 1

df3 = pd.DataFrame.from_dict(percentages, orient="index", columns = ["Symbol", "Owned Percentage"])

df = pd.merge(df1, df2, on=["Symbol"])
df = pd.merge(df, df3, on=["Symbol"])

df_for_computation = df.copy()

df_for_computation = df_for_computation.assign(sortval = df_for_computation["Owned Percentage"] - df_for_computation["Desired Percentage"]).sort_values('sortval').drop('sortval', 1)

st.table(df_for_computation)

for i in range(len(df_for_computation)):
    print(df_for_computation.iloc[i]["Symbol"])

df = df[["Symbol", "Name", "Quantity", "Current Price", "Owned Percentage", "Desired Percentage"]]

st.table(df)