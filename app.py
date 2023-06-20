import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sn
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Prediction", page_icon=":fire:")
st.title("🌎 Stocks Prediction")

df=pd.read_csv('GOOG.csv')


df['year'] = pd.to_datetime(df['date']).dt.strftime('%Y')

year=st.selectbox("Select Year",options=df['year'].unique())
df_selection=df.query("year==@year")
st.dataframe(df_selection)

#No of stocks traded
st.title('Stocks Traded')
st.area_chart(df_selection,x='date',y=['volume'])
y=str(year)
ll="The highest volume of stocks sold in "+y+ " is "+str(df_selection['volume'].max(numeric_only = True))+" on "+str(df.loc[df['volume'] == df_selection['volume'].max(numeric_only = True), 'date'].values)
st.write("**Insights:**")
st.write(ll)
tl="The lowest volume of stocks sold in "+y+ " is "+str(df_selection['volume'].min(numeric_only = True))+" on "+str(df.loc[df['volume'] == df_selection['volume'].min(numeric_only = True), 'date'].values)
st.write(tl)

s_traded=px.scatter(df_selection,x="date",y="volume",animation_frame="date",range_x=["2016-01-01", "2023-04-01"],range_y=[100,14000000],title="Stocks Traded(Animation)")

s_traded.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 80
s_traded.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 80

st.plotly_chart(s_traded)

#high stock price
high=px.line(df_selection,x="date",y="high",title="High Price of Stock")
st.plotly_chart(high)
st.write("**Insights:**")
ll="The stock price reached its maximum of "+ str(df_selection['high'].max(numeric_only = True))+ " in "+ y + " during the month of "+str(df.loc[df['high'] == df_selection['high'].max(numeric_only = True), 'month'].values)
st.write(ll)



#low stock price
low=px.line(df_selection,x="date",y="low",title="Low Price of Stock")
st.plotly_chart(low)
st.write("**Insights:**")
tl="The stock price reached its minimum of "+ str(df_selection['low'].min(numeric_only = True))+ " in "+ y + " during the month of "+str(df.loc[df['low'] == df_selection['low'].min(numeric_only = True), 'month'].values)
st.write(tl)


#Heatmaps
cmap = "tab20"
df_s=pd.read_csv('GOOG.csv',usecols=[3,6,7,8,11,12])

st.title("Heatmap between Attributes")
fig, ax = plt.subplots()
sn.heatmap(df_s.corr(numeric_only = True),annot = True, fmt='.1g',cmap= 'coolwarm', ax=ax)
st.write(fig)
st.write("**Insights:**")
st.write("if the value between the attributes is greater than zero then it denotes a direct proportion between them")
st.write("if the value between the attributes is less than zero then it denotes a inverse proportion between them")


#plot between variables
left_column, right_column = st.columns(2)
with left_column:
    x=st.selectbox("Select x axis",options=['date','low','high','adjClose','volume','close','adjOpen'])
with right_column:
    y=st.selectbox("Select y axis",options=['high','low','date','adjClose','volume','close','adjOpen'])

test=px.bar(df_selection,x,y,title="Selected Plot")
st.plotly_chart(test)



#price in each month
p_month = df_selection.groupby(by=["month"]).mean(numeric_only=True)[["low"]]
p_month_bar = px.bar(
    p_month,
    x=p_month.index,
    y='low',
    title="<b>Average Price</b>",
    color_discrete_sequence=["#0083B8"] * len(p_month),
    template="plotly_white",
)
st.plotly_chart(p_month_bar)
st.write("**Insights:**")
ll="The highest average price of a stock is  " +str(p_month['low'].max(numeric_only = True))
tl="The lowest average price of a stock is  " +str(p_month['low'].min(numeric_only = True))
st.write(ll)
st.write(tl)

