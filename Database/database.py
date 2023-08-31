# packages
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import streamlit as st
from dotenv import load_dotenv
from scraping_scripts import fx_calendar, fetch_currencies, fetch_stocks, fetch_commodities, fetch_bonds, fetch_crypto, fetch_earnings

from deta import Deta
DETA_KEY_ECON_DASHBOARD = "INSERT_DETASPACE_DB_KEY"
deta_dashboard = Deta(DETA_KEY_ECON_DASHBOARD)

db_calendar = deta_dashboard.Base("daily_forex_calendar")
db_currency = deta_dashboard.Base("daily_currency")
db_stocks = deta_dashboard.Base("daily_stocks")
db_commodities = deta_dashboard.Base("daily_commodities")
db_bonds = deta_dashboard.Base("daily_bonds")
db_crypto = deta_dashboard.Base("daily_crypto")
db_earnings = deta_dashboard.Base("daily_earnings")

# (CALENDAR)
def insert_calendar():
    data = fx_calendar()
    time = data["time"]
    currency = data["currency"]
    event = data["event"]
    actual = data["actual"]
    consensus = data["consensus"]
    forecast = data["forecast"]
    previous = data["previous"]
    return db_calendar.put({"time":time.tolist(), "currency":currency.tolist(),
                   "event":event.tolist(), "actual":actual.tolist(),
                   "consensus":consensus.tolist(),"forecast":forecast.tolist(),
                   "previous":previous.tolist()})
# (CALENDAR)
def get_calendar():
    data = db_calendar.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["time", "currency", "event", "actual", "consensus", "forecast", "previous"]
    data = data[columns_to_select]
    return data
# (CALENDAR)
def update_calendar():
    data = fx_calendar()
    time = data["time"]
    currency = data["currency"]
    event = data["event"]
    actual = data["actual"]
    consensus = data["consensus"]
    forecast = data["forecast"]
    previous = data["previous"]

    return db_calendar.put({"time":time.tolist(), "currency":currency.tolist(),
                   "event":event.tolist(), "actual":actual.tolist(),
                   "consensus":consensus.tolist(),"forecast":forecast.tolist(),
                   "previous":previous.tolist()},key="1xs953alc6ee")


# (CURRENCY)
def insert_currency():
    data = fetch_currencies()
    pairs = data["pairs"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_currency.put({
        "pairs":pairs.tolist(),"price":price.tolist(),
        "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
        "monthly":monthly.tolist(), "yoy":yoy.tolist()})
# (CURRENCY)
def get_currencies():
    data = db_currency.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["pairs", "price", "percentage_change", "weekly", "monthly", "yoy"]
    data = data[columns_to_select]
    return data
# (CURRENCY)
def update_currency():
    data = fetch_currencies()
    pairs = data["pairs"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_currency.put({
        "pairs": pairs.tolist(),
        "price": price.tolist(),
        "percentage_change": percentage_change.tolist(),
        "weekly": weekly.tolist(),
        "monthly": monthly.tolist(),
        "yoy": yoy.tolist()
    }, key="f58wghu8vxnj")


# (STOCKS)
def insert_stocks():
    data = fetch_stocks()
    indice = data["indice"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_stocks.put({"indice":indice.tolist(),"price":price.tolist(),
                            "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
                            "monthly":monthly.tolist(), "yoy":yoy.tolist()})    
# (STOCKS)
def get_stocks():
    data = db_stocks.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["indice", "price", "percentage_change", "weekly", "monthly", "yoy"]
    data = data[columns_to_select]
    return data
# (STOCKS)
def update_stocks():
    data = fetch_stocks()
    indice = data["indice"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_stocks.put({"indice":indice.tolist(),"price":price.tolist(),
                            "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
                            "monthly":monthly.tolist(), "yoy":yoy.tolist()}, key="m28hc4otuhqf") 


# (COMMODITY)
def insert_commodities():  
    data = fetch_commodities()
    commodity = data["commodity"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_commodities.put({"commodity":commodity.tolist(),"price":price.tolist(),
                            "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
                            "monthly":monthly.tolist(), "yoy":yoy.tolist()})   
# (COMMODITY)
def get_commodities():
    data = db_stocks.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["commodity", "price", "percentage_change", "weekly", "monthly", "yoy"]
    data = data[columns_to_select]
    return data
# (COMMODITY)
def update_commodities():
    data = fetch_commodities()
    commodity = data["commodity"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_commodities.put({"commodity":commodity.tolist(),"price":price.tolist(),
                            "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
                            "monthly":monthly.tolist(), "yoy":yoy.tolist()},key="2irpii2q3vnx")    


# (BONDS)
def insert_bonds():
    data = fetch_bonds()
    Y_10 = data["Y_10"]
    yields = data["yields"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_bonds.put({"Y_10":Y_10.tolist(),"yields":yields.tolist(),
                                "weekly":weekly.tolist(),"monthly":monthly.tolist(), 
                                "yoy":yoy.tolist()})      
# (BONDS)
def get_bonds():
    data = db_bonds.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["10Y", "yields", "weekly", "monthly", "yoy"]
    data = data[columns_to_select]
    return data   
# (BONDS)
def update_bonds():
    data = fetch_bonds()
    Y_10 = data["Y_10"]
    yields = data["yields"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    return db_bonds.put({"Y_10":Y_10.tolist(),"yields":yields.tolist(),
                                "weekly":weekly.tolist(),"monthly":monthly.tolist(), 
                                "yoy":yoy.tolist()}, key="f14b8z16eo9k")      


# (CRYPTO)
def insert_crypto():
    data = fetch_crypto()
    currency = data["currency"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    marketcap = data["marketcap"]
    return db_crypto.put({"currency":currency.tolist(),"price":price.tolist(),
                            "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
                            "monthly":monthly.tolist(), "yoy":yoy.tolist(),
                            "marketcap":marketcap.tolist()})    
# (CRYPTO)
def get_crypto():
    data = db_crypto.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["currency", "price", "percentage_change", "weekly", "monthly", "yoy","marketcap"]
    data = data[columns_to_select]
    return data
# (CRYPTO)
def update_crypto():
    data = fetch_crypto()
    currency = data["currency"]
    price = data["price"]
    percentage_change = data["percentage_change"]
    weekly = data["weekly"]
    monthly = data["monthly"]
    yoy = data["yoy"]
    marketcap = data["marketcap"]
    return db_crypto.put({"currency":currency.tolist(),"price":price.tolist(),
                            "percentage_change":percentage_change.tolist(),"weekly":weekly.tolist(),
                            "monthly":monthly.tolist(), "yoy":yoy.tolist(),
                            "marketcap":marketcap.tolist()}, key="hihy4ph27jkj") 


# (EARNINGS)
def insert_earnings():
    data = fetch_earnings()
    company_name = data["company_name"]
    eps = data["eps"]
    consensus = data["consensus"]
    previous = data["previous"]
    revenue = data["revenue"]
    forecast = data["forecast"]
    marketcap = data["marketcap"]
    fiscal = data["fiscal"]
    return db_earnings.put({"company_name":company_name.tolist(), "eps":eps.tolist(),
                            "consensus":consensus.tolist(), "previous":previous.tolist(),
                            "revenue":revenue.tolist(),"forecast":forecast.tolist(), 
                            "marketcap":marketcap.tolist(),"fiscal":fiscal.tolist()})
# (EARNINGS)
def get_earnings():
    data = db_earnings.fetch().items
    data = pd.DataFrame(data)
    data = data.apply(pd.Series.explode)
    columns_to_select = ["company_name", "eps", "consensus", "previous", "revenue", "forecast", "marketcap","fiscal"]
    data = data[columns_to_select]
    return data
# (EARNINGS)
def update_earnings():
    data = fetch_earnings()
    company_name = data["company_name"]
    eps = data["eps"]
    consensus = data["consensus"]
    previous = data["previous"]
    revenue = data["revenue"]
    forecast = data["forecast"]
    marketcap = data["marketcap"]
    fiscal = data["fiscal"]
    return db_earnings.put({"company_name":company_name.tolist(), "eps":eps.tolist(),
                            "consensus":consensus.tolist(), "previous":previous.tolist(),
                            "revenue":revenue.tolist(),"forecast":forecast.tolist(), 
                            "marketcap":marketcap.tolist(),"fiscal":fiscal.tolist()}, key="ckiwvealzl04")
