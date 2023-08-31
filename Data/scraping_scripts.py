import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import streamlit as st
import time 

def fx_calendar():
    url = "https://tradingeconomics.com/calendar"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)
    
    table_data = driver.find_element(By.XPATH,'//div[3][@class="table-responsive panel panel-default"]')
    container = table_data.find_elements(By.XPATH,'//tr[@data-url]')
    
    times=[]
    currency=[]
    event=[]
    actual=[]
    previous=[]
    consensus=[]
    forecast=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()


    num_items = len(container)
    for i,contain in enumerate(container):
        times.append(contain.find_element(By.XPATH,'./td[1]').text)
        currency.append(contain.find_element(By.XPATH,'./td[2]').text)
        event.append(contain.find_element(By.XPATH,'./td[3]').text)
        actual.append(contain.find_element(By.XPATH,'./td[4]').text)
        previous.append(contain.find_element(By.XPATH,'./td[5]').text)
        consensus.append(contain.find_element(By.XPATH,'./td[6]').text)
        forecast.append(contain.find_element(By.XPATH,'./td[7]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text} {i+1}/{num_items}")

    driver.quit()    

    progress_bar.empty()
    progress_text_placeholder.empty()

    data = pd.DataFrame({"time":times,
                        "currency":currency,
                        "event":event,
                        "actual":actual,
                        "consensus":consensus,
                        "forecast":forecast,
                        "previous":previous})
    return data

def fetch_currencies():
    url="https://tradingeconomics.com/currencies"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)


    table_data = driver.find_element(By.XPATH,'//div[@class="panel panel-default"]')
    container = table_data.find_elements(By.XPATH,'//tbody[1]//tr')

    pairs=[]
    price=[]
    percentage_change=[]
    weekly=[]
    monthly=[]
    yoy=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()

    num_items = len(container)
    for i,contain in enumerate(container):
        pairs.append(contain.find_element(By.XPATH,'./td[1]').text)
        price.append(contain.find_element(By.XPATH,'./td[2]').text)
        percentage_change.append(contain.find_element(By.XPATH,'./td[3]').text)
        weekly.append(contain.find_element(By.XPATH,'./td[4]').text)
        monthly.append(contain.find_element(By.XPATH,'./td[5]').text)
        yoy.append(contain.find_element(By.XPATH,'./td[6]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text} {i+1}/{num_items}")

    driver.quit()

    progress_bar.empty()
    progress_text_placeholder.empty()

    data = pd.DataFrame({"pairs":pairs,
                        "price":price,
                        "percentage_change":percentage_change,
                        "weekly":weekly,
                        "monthly":monthly,
                        "yoy":yoy})
    return data
    
def fetch_stocks():
    url="https://tradingeconomics.com/stocks"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)

    table_data = driver.find_element(By.XPATH,'//div[@class="col-lg-10"]')
    container = table_data.find_elements(By.XPATH,'//tbody[1]//tr')

    indice=[]
    price=[]
    percentage_change=[]
    weekly=[]
    monthly=[]
    yoy=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()

    num_items=len(container)
    for i,contain in enumerate(container):
        indice.append(contain.find_element(By.XPATH, './td[2]').text)
        price.append(contain.find_element(By.XPATH, './td[3]').text)
        percentage_change.append(contain.find_element(By.XPATH, './td[5]').text)
        weekly.append(contain.find_element(By.XPATH, './td[6]').text)
        monthly.append(contain.find_element(By.XPATH, './td[7]').text)
        yoy.append(contain.find_element(By.XPATH, './td[8]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text}{i+1}/{num_items}")

    driver.quit()

    progress_bar.empty()
    progress_text_placeholder.empty()

    data = pd.DataFrame({"indice":indice,
                        "price":price,
                        "percentage_change":percentage_change,
                        "weekly":weekly,
                        "monthly":monthly,
                        "yoy":yoy})
    return data

def fetch_commodities():
    url="https://tradingeconomics.com/commodities"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)

    table_data = driver.find_element(By.XPATH,'//div[@class="col-lg-10"]')
    container = table_data.find_elements(By.XPATH,'//tbody[1]//tr')

    commodity=[]
    price=[]
    percentage_change=[]
    weekly=[]
    monthly=[]
    yoy=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()

    num_items=len(container)
    for i,contain in enumerate(container):
        commodity.append(contain.find_element(By.XPATH,'./td[1]').text)
        price.append(contain.find_element(By.XPATH,'./td[2]').text)
        percentage_change.append(contain.find_element(By.XPATH,'./td[4]').text)
        weekly.append(contain.find_element(By.XPATH,'./td[5]').text)
        monthly.append(contain.find_element(By.XPATH,'./td[6]').text)
        yoy.append(contain.find_element(By.XPATH,'./td[7]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text} {i+1}/{num_items}")
    driver.quit()

    progress_bar.empty()
    progress_text_placeholder.empty()

    data = pd.DataFrame({"commodity":commodity,
                        "price":price,
                        "percentage_change":percentage_change,
                        "weekly":weekly,
                        "monthly":monthly,
                        "yoy":yoy})
    data["commodity"] = data["commodity"].str.replace("\nUSD"," ")
    data["commodity"] = data["commodity"].str.replace("\nGBP"," ")
    data["commodity"] = data["commodity"].str.replace("\nEUR"," ")
    return data

def fetch_bonds():
    url="https://tradingeconomics.com/bonds"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)

    table_data = driver.find_element(By.XPATH,'(//table[@class="table table-hover table-striped table-heatmap"])[1]')
    container = table_data.find_elements(By.XPATH,'.//tbody//tr')

    Y_10 = []
    yields=[]
    weekly=[]
    monthly=[]
    yoy=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()

    num_items=len(container)
    for i,contain in enumerate(container):
        Y_10.append(contain.find_element(By.XPATH,'./td[2]').text)
        yields.append(contain.find_element(By.XPATH,'./td[3]').text)
        weekly.append(contain.find_element(By.XPATH,'./td[5]').text)
        monthly.append(contain.find_element(By.XPATH,'./td[6]').text)
        yoy.append(contain.find_element(By.XPATH,'./td[7]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text}{i+1}/{num_items}")
    driver.quit()

    progress_bar.empty()
    progress_text_placeholder.empty()

    data = pd.DataFrame({"10Year":Y_10,
                        "yields":yields,
                        "weekly":weekly,
                        "monthly":monthly,
                        "yoy":yoy})
    return data

def fetch_crypto():
    url="https://tradingeconomics.com/crypto"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)

    table_data = driver.find_element(By.XPATH,'(//table[@class="table table-hover table-striped table-heatmap"])[1]')
    container = table_data.find_elements(By.XPATH,'.//tbody//tr')

    currency=[]
    price=[]
    percentage_change=[]
    weekly=[]
    monthly=[]
    yoy=[]
    marketcap=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()

    num_items=len(container)
    for i,contain in enumerate(container):
        currency.append(contain.find_element(By.XPATH, './td[1]').text)
        price.append(contain.find_element(By.XPATH, './td[2]').text)
        percentage_change.append(contain.find_element(By.XPATH, './td[4]').text)
        weekly.append(contain.find_element(By.XPATH, './td[5]').text)
        monthly.append(contain.find_element(By.XPATH, './td[6]').text)
        yoy.append(contain.find_element(By.XPATH, './td[7]').text)
        marketcap.append(contain.find_element(By.XPATH, './td[8]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text}{i+1}/{num_items}")

    driver.quit()
    progress_bar.empty()
    progress_text_placeholder.empty()
    data = pd.DataFrame({"currency":currency,
                        "price":price,
                        "percentage_change":percentage_change,
                        "weekly":weekly,
                        "monthly":monthly,
                        "yoy":yoy,
                        "marketcap":marketcap})
    return data

def fetch_earnings():
    url="https://tradingeconomics.com/earnings"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(url)

    table_data = driver.find_element(By.XPATH,'//table[@class="table table-hover table-condensed table-stripped"]')
    container = table_data.find_elements(By.XPATH,'.//tbody//tr')

    company_name = []
    eps = []
    consensus=[]
    previous=[]
    revenue=[]
    forecast=[]
    marketcap=[]
    fiscal=[]

    progress_text = "Operation in progress. Please wait."
    progress_bar  = st.progress(0)
    progress_text_placeholder = st.empty()

    num_items=len(container)
    for i,contain in enumerate(container):
        company_name.append(contain.find_element(By.XPATH,'./td[2]').text)
        eps.append(contain.find_element(By.XPATH,'./td[3]').text)
        consensus.append(contain.find_element(By.XPATH,'./td[4]').text)
        previous.append(contain.find_element(By.XPATH,'./td[5]').text)
        revenue.append(contain.find_element(By.XPATH,'./td[6]').text)
        forecast.append(contain.find_element(By.XPATH,'./td[7]').text)
        marketcap.append(contain.find_element(By.XPATH,'./td[9]').text)
        fiscal.append(contain.find_element(By.XPATH,'./td[10]').text)
        progress_bar.progress((i+1)/num_items)
        progress_text_placeholder.text(f"{progress_text}{i+1}/{num_items}")
    driver.quit()

    progress_bar.empty()
    progress_text_placeholder.empty()

    data = pd.DataFrame({"company_name":company_name,
                        "eps":eps,
                        "consensus":consensus,
                        "previous":previous,
                        "revenue":revenue,
                        "forecast":forecast,
                        "marketcap":marketcap,
                        "fiscal":fiscal})
    return data       