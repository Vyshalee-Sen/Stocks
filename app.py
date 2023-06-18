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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dropout,Dense

dataset_train = pd.read_csv("C:\\1.SHALU\CIT\Sem_4\DS\Project\GOOG.csv")
training_set = dataset_train.iloc[:, 2:3].values

sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
y_train = []

for i in range(60, 1219):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

regressor = Sequential()

regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1))

regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

print(regressor.summary())

regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)

dataset_test = pd.read_csv("C:\\1.SHALU\CIT\Sem_4\DS\Project\GOOG_test.csv")
real_stock_price = dataset_test.iloc[:, 2:3].values

# Getting the predicted stock price of 2017
dataset_total = pd.concat((dataset_train['open'], dataset_test['open']), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 100):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualising the results
grp=plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()
