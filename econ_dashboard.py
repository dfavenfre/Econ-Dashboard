from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.models import load_model
import pickle
import datetime
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime
import yfinance as yf
import pandas as pd
from scraping_scripts import fx_calendar, fetch_currencies, fetch_stocks, fetch_commodities, fetch_bonds, fetch_crypto, fetch_earnings
import joblib
import tensorflow as tf
import tensorflow_hub as hub


# Welcome to Econ Dashboard (Beta) 
title_html = """
    <h1 style="color:black; font-size:36px;">Welcome to Econ Dashboard <span style="font-size:14px;">BETA</span></h1>
"""
st.sidebar.markdown(title_html, unsafe_allow_html=True)

# About Econ-Dashboard
sidebar_text_style = """
    font-size: 16px;
    line-height: 1.5;
    text-align: justify;
"""
st.sidebar.markdown(
    """
    <div style="{}">
        <h3>About Econ Dashboard</h3>
        <ul>
            <li> A centralized dashboard for screening and downloading Stock/ETF/FX/Economic Data, as well as viewing Forex, Metal, Energy, and Crypto Calendars.</li>
        </ul>
    """.format(sidebar_text_style),
    unsafe_allow_html=True
)

# Social Hubs
st.sidebar.markdown(

    """
    <div stlye="{}">
        <h3> Follow My Social Hubs For More Content </h3>
        <ul>
            <li><a href="https://medium.com/@bauglir">Medium</a></li>
            <li><a href="https://www.kaggle.com/dfavenfre">Kaggle</a></li>
            <li><a href="https://github.com/dfavenfre">GitHub</a></li>
            <li><a href="https://www.linkedin.com/in/tolga-%C5%9Fakar-575b86136">LinkedIn</a></li>
         </ul>  
    
    """, unsafe_allow_html=True

)

### Stock Screener
st.title("Stock Sceener")
st.write(
    """
    Stock Screener Is Equipped With YahooFinanceAPI. You Can Directly Use Any Ticker/Symbol From https://finance.yahoo.com. You Can Download The Data After Running The Screener
    """
)


# Date and Interval
selected_date = st.date_input("Select A Date", 
                  value=datetime.today().date(),
                  min_value=datetime(2000, 1, 1).date(),
                  max_value=datetime.today().date())
selected_timeframe = st.selectbox("Select A Time Frame",
                                         ["5m","15m","1h","1d"])

def convert_df(df):
    return df.to_csv().encode('utf-8')

if 'ticker_df' not in st.session_state:
    st.session_state.ticker_df = None

# Display Ticker/Symbol
with st.form(key="Sceener"):
    name = st.text_input(label="Write Ticker/Symbol")
    submit = st.form_submit_button(label="Process The Screener")

if submit:
    tickerData = yf.Ticker(name)
    ticker_df = tickerData.history(interval=selected_timeframe, start=selected_date)
    st.session_state.ticker_df = ticker_df

if st.session_state.ticker_df is not None:
    ticker_df = st.session_state.ticker_df

    # display sp500 close and volume data
    st.write(str(name) + " " + selected_timeframe + " Close Data")
    fig_close = go.Figure(data=[go.Candlestick(x=ticker_df.index,
                                               open=ticker_df.Open,
                                               high=ticker_df.High,
                                               low=ticker_df.Low,
                                               close=ticker_df.Close)])
    st.plotly_chart(fig_close)
    
    csv = convert_df(ticker_df)
    st.download_button(
        label="Download Ticker Data",
        data=csv,
        file_name='ticker_dataframe.csv',
        mime='text/csv',
    )

### Economic Calendar
st.title("Data Provider")
st.write(
    
    """
    Access a professional-grade calendar featuring daily updates on Economic Calendar, Forex, Stocks, Commodities, Bonds, and Crypto and Earnings, including comprehensive news, actual, forecast, and previous announcements.
    """
)

data_option = st.selectbox("Select Data", ["Forex Calendar","FX Market","Stock Market", "Commodities","Bonds","Crypto","Earnings"])

if data_option == "Forex Calendar":
    if st.button("Get Data"):
        calendar_data = fx_calendar()
        st.dataframe(calendar_data, width=800)
        csv = convert_df(calendar_data)
        st.download_button(
            label="Download Calendar data",
            data=csv,
            file_name='fx_calendar.csv',
            mime='text/csv',
        )
if data_option == "FX Market":
    if st.button("Get Data"):
        currency_data = fetch_currencies()
        st.dataframe(currency_data, width=800)  
        csv = convert_df(currency_data)
        st.download_button(
            label="Download currency data",
            data=csv,
            file_name='currency.csv',
            mime='text/csv',
        ) 
if data_option == "Stock Market":
    if st.button("Get Data"):
        stocks_data = fetch_stocks()
        st.dataframe(stocks_data, width=800)
        csv = convert_df(stocks_data)
        st.download_button(
            label="Download stocks data",
            data=csv,
            file_name='stocks.csv',
            mime='text/csv',
        )         
if data_option == "Commodities":
    if st.button("Get Data"):
        commodity_data = fetch_commodities()
        st.dataframe(commodity_data, width=800)
        csv = convert_df(commodity_data)
        st.download_button(
            label="Download commodity data",
            data=csv,
            file_name='commodities.csv',
            mime='text/csv',
        )         
if data_option == "Bonds":
    if st.button("Get Data"):
        bonds_data = fetch_bonds()
        st.dataframe(bonds_data, width=800)
        csv = convert_df(bonds_data)
        st.download_button(
            label="Download bonds data",
            data=csv,
            file_name='bonds.csv',
            mime='text/csv',
        )         
if data_option == "Crypto":
    if st.button("Get Data"):
        crypto_data = fetch_crypto()
        st.dataframe(crypto_data, width=800)  
        csv = convert_df(crypto_data)
        st.download_button(
            label="Download cryptocurrency data",
            data=csv,
            file_name='crypto.csv',
            mime='text/csv',
        )         
if data_option == "Earnings":
    if st.button("Get Data"):
        earnings_data = fetch_earnings()
        st.dataframe(earnings_data, width=800)
        csv = convert_df(earnings_data)
        st.download_button(
            label="Download earnings data",
            data=csv,
            file_name='earnings.csv',
            mime='text/csv',
        )   

### Sentiment Analysis

st.title("Sentiment Analysis")


import joblib
import tensorflow as tf
import tensorflow_hub as hub

# Define the custom layer
class USEEncoderLayer(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(USEEncoderLayer, self).__init__(**kwargs)
        self.use_layer = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder/4",
                                        input_shape=[],  # check the important notes
                                        dtype=tf.string,
                                        trainable=False,
                                        name="USE_encoder")

    def call(self, inputs, **kwargs):
        return self.use_layer(inputs)

# Register the custom layer
custom_objects = {"USEEncoderLayer": USEEncoderLayer, "KerasLayer": hub.KerasLayer}

# Load the model with custom layer
with tf.keras.utils.custom_object_scope(custom_objects):
    best_use_model = tf.keras.models.load_model(r"C:\Users\Tolga\Desktop\streamlit apps\econ_dashboard\model_use.hdf5")

import numpy as np
# Function to make prediction on new text
def predict_sentiment(text):
    # Make prediction
    prediction = tf.squeeze(best_use_model.predict([text]))
    return prediction

def get_sentiment_label(pred):
    sentiment_label = ["Negative", "Neutral", "Positive"]
    max_index = np.argmax(pred.numpy())
    return sentiment_label[max_index]

text_input = st.text_area("Enter the text:", value='')
submit_button = st.button("Predict")

if submit_button and text_input:
    # Make prediction
    prediction = predict_sentiment(text_input)
    sentiment_label = get_sentiment_label(prediction)
    confidence = np.max(prediction) * 100
    # Output the result
    output = f"{sentiment_label.capitalize()} : [Confidence: {confidence:.2f}%]"
    
    # Display the result
    st.write('Prediction Results:')
    st.write(f'Sentiment Label: {sentiment_label.capitalize()}')
    st.write(f'Confidence: {confidence:.2f}%')
    st.write('Prediction Probabilities:')
    sentiment_labels = ["Negative", "Neutral", "Positive"]
    for class_idx, prob in enumerate(prediction):
        st.write(f'{sentiment_labels[class_idx]}: {prob:.4f}')
