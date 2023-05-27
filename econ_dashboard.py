# packages
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
from database import get_calendar, update_calendar, get_currencies, update_currency, get_stocks, update_stocks, get_commodities, update_commodities, get_bonds, update_bonds, get_crypto, update_crypto, get_earnings, update_earnings
import os

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

# Side-bar Warning
st.sidebar.write(
    """
    **Select A Time Interval and Time Frame**
    """
)
# Date and Interval
selected_date = st.date_input("Select A Date", 
                  value=datetime.today().date(),
                  min_value=datetime(2000, 1, 1).date(),
                  max_value=datetime.today().date())
selected_timeframe = st.selectbox("Select A Time Frame",
                                         ["5m","15m","1h","1d"])

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
st.title("Economic Calendar")
st.write(
    
    """
    Access a professional-grade calendar featuring daily updates on Economic Calendar, Forex, Stocks, Commodities, Bonds, and Crypto and Earnings, including comprehensive news, actual, forecast, and previous announcements.
    """
)


from deta import Deta
DETA_KEY_ECON_DASHBOARD = st.secrets["dashboard_db"]
deta_dashboard = Deta(DETA_KEY_ECON_DASHBOARD)
db_calendar = deta_dashboard.Base("daily_forex_calendar")
db_currency = deta_dashboard.Base("daily_currency")
db_stocks = deta_dashboard.Base("daily_stocks")
db_commodities = deta_dashboard.Base("daily_commodities")
db_bonds = deta_dashboard.Base("daily_bonds")
db_crypto = deta_dashboard.Base("daily_crypto")
db_earnings = deta_dashboard.Base("daily_earnings")

data_option = st.selectbox("Select Data", ["Forex Calendar","FX Market","Stock Market", "Commodities","Bonds","Crypto","Earnings"])

if data_option == "Forex Calendar":
    if st.button("Get Data"):
        calendar_data = get_calendar()
        st.dataframe(calendar_data, width=800)

if data_option == "FX Market":
    if st.button("Get Data"):
        currency_data = get_currencies()
        st.dataframe(currency_data, width=800)   

if data_option == "Stock Market":
    if st.button("Get Data"):
        stocks_data = get_stocks()
        st.dataframe(stocks_data, width=800)  

if data_option == "Commodities":
    if st.button("Get Data"):
        commodity_data = get_commodities()
        st.dataframe(commodity_data, width=800)  

if data_option == "Bonds":
    if st.button("Get Data"):
        bonds_data = get_bonds()
        st.dataframe(bonds_data, width=800)  

if data_option == "Crypto":
    if st.button("Get Data"):
        crypto_data = get_crypto()
        st.dataframe(crypto_data, width=800)  

if data_option == "Earnings":
    if st.button("Get Data"):
        earnings_data = get_earnings()
        st.dataframe(earnings_data, width=800)  
