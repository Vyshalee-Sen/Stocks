import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Stock Prediction", page_icon=":fire:")
st.title("🌎 Stocks Prediction")

df=pd.read_csv('GOOG.csv')


df['year'] = pd.to_datetime(df['date']).dt.strftime('%Y')

year=st.selectbox("Select Year",options=df['year'].unique())
df_selection=df.query("year==@year")
st.dataframe(df_selection)

#No of stocks traded
s_traded=px.scatter(df_selection,x="date",y="volume",animation_frame="date",range_x=["2016-01-01", "2023-04-01"],range_y=[100,14000000],title="Stocks Traded")


s=px.line(df_selection,x="date",y="volume",title="Stocks Traded")



st.plotly_chart(s)

s_traded.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 80
s_traded.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 80

st.plotly_chart(s_traded)




st.plotly_chart(grp)
