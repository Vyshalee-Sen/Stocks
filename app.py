import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Stock Prediction", page_icon=":fire:")

df=pd.read_csv('GOOG.csv')
st.dataframe(df)

date=df['date']
vol=df['volume']

#No of stocks traded
s_traded=px.scatter(df,x="date",y=vol,animation_frame="date",range_x=["2016-01-01", "2023-04-01"],range_y=[100,14000000],title="Stocks Traded")


s=px.line(df,x=date,y=vol,title="Stocks Traded")


#st.write(date_range)


st.plotly_chart(s)

s_traded.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 80
s_traded.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 80

st.plotly_chart(s_traded)
