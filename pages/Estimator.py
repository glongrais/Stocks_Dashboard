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

df_for_computation = df_for_computation.assign(sortval = df_for_computation["Owned Percentage"] - df_for_computation["Desired Percentage"]).sort_values('sortval')#.drop('sortval', 1)

to_buy_number = {}

total_amount_eur = 0

for i in range(df.shape[0]):
    if df_for_computation.iloc[i]["sortval"] < 0:
        to_buy_eur = to_compute * df_for_computation.iloc[i]["sortval"] * -0.01
        if to_buy_eur < 100:
            to_buy_number[df_for_computation.iloc[i]["Symbol"]] = (df_for_computation.iloc[i]["Symbol"], 0)
        else:
            if to_buy_eur < value:
                amount = int(to_buy_eur/df_for_computation.iloc[i]["Current Price"])
                to_buy_number[df_for_computation.iloc[i]["Symbol"]] = (df_for_computation.iloc[i]["Symbol"], amount)

                value -= amount*df_for_computation.iloc[i]["Current Price"]

                total_amount_eur += amount*df_for_computation.iloc[i]["Current Price"]
            else:
                amount = int(value/df_for_computation.iloc[i]["Current Price"])
                to_buy_number[df_for_computation.iloc[i]["Symbol"]] = (df_for_computation.iloc[i]["Symbol"], amount)

                value -= amount*df_for_computation.iloc[i]["Current Price"]

                total_amount_eur += amount*df_for_computation.iloc[i]["Current Price"]
    else:
        to_buy_number[df_for_computation.iloc[i]["Symbol"]] = (df_for_computation.iloc[i]["Symbol"], 0)

df4 = pd.DataFrame.from_dict(to_buy_number, orient="index", columns = ["Symbol", "To Buy"])

df = pd.merge(df, df4, on=["Symbol"])

df = df[["Symbol", "Name", "Quantity", "To Buy", "Current Price", "Owned Percentage", "Desired Percentage"]]

st.table(df)
st.write(total_amount_eur)