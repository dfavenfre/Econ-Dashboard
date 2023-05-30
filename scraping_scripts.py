import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def fx_calendar():
    url = "https://tradingeconomics.com/calendar"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Added for running in a virtual environment

    # Set up virtual display using XVFB (X Virtual Frame Buffer)
    xvfb_options = ["xvfb-run", "--auto-servernum", "--server-args='-screen 0 1920x1080x24'"]
    driver = webdriver.Chrome(executable_path="/usr/bin/google-chrome", options=chrome_options, service_args=xvfb_options)
    
    driver.get(url)
    
    # Wait for the table to be loaded
    table_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[3][@class="table-responsive panel panel-default"]')))
    
    container = table_data.find_elements(By.XPATH, '//tr[@data-url]')
    
    time = []
    currency = []
    event = []
    actual = []
    previous = []
    consensus = []
    forecast = []
  
    for contain in container:
        time.append(contain.find_element(By.XPATH, './td[1]').text)
        currency.append(contain.find_element(By.XPATH, './td[2]').text)
        event.append(contain.find_element(By.XPATH, './td[3]').text)
        actual.append(contain.find_element(By.XPATH, './td[4]').text)
        previous.append(contain.find_element(By.XPATH, './td[5]').text)
        consensus.append(contain.find_element(By.XPATH, './td[6]').text)
        forecast.append(contain.find_element(By.XPATH, './td[7]').text)

    driver.quit()

    data = pd.DataFrame({
        "time": time,
        "currency": currency,
        "event": event,
        "actual": actual,
        "consensus": consensus,
        "forecast": forecast,
        "previous": previous
    })
    
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

    for contain in container:
        pairs.append(contain.find_element(By.XPATH,'./td[1]').text)
        price.append(contain.find_element(By.XPATH,'./td[2]').text)
        percentage_change.append(contain.find_element(By.XPATH,'./td[3]').text)
        weekly.append(contain.find_element(By.XPATH,'./td[4]').text)
        monthly.append(contain.find_element(By.XPATH,'./td[5]').text)
        yoy.append(contain.find_element(By.XPATH,'./td[6]').text)

    driver.quit()

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

    for contain in container:
        indice.append(contain.find_element(By.XPATH, './td[2]').text)
        price.append(contain.find_element(By.XPATH, './td[3]').text)
        percentage_change.append(contain.find_element(By.XPATH, './td[5]').text)
        weekly.append(contain.find_element(By.XPATH, './td[6]').text)
        monthly.append(contain.find_element(By.XPATH, './td[7]').text)
        yoy.append(contain.find_element(By.XPATH, './td[8]').text)

    driver.quit()

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

    for contain in container:
        commodity.append(contain.find_element(By.XPATH,'./td[1]').text)
        price.append(contain.find_element(By.XPATH,'./td[2]').text)
        percentage_change.append(contain.find_element(By.XPATH,'./td[4]').text)
        weekly.append(contain.find_element(By.XPATH,'./td[5]').text)
        monthly.append(contain.find_element(By.XPATH,'./td[6]').text)
        yoy.append(contain.find_element(By.XPATH,'./td[7]').text)

    driver.quit()

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

    for contain in container:
        Y_10.append(contain.find_element(By.XPATH,'./td[2]').text)
        yields.append(contain.find_element(By.XPATH,'./td[3]').text)
        weekly.append(contain.find_element(By.XPATH,'./td[5]').text)
        monthly.append(contain.find_element(By.XPATH,'./td[6]').text)
        yoy.append(contain.find_element(By.XPATH,'./td[7]').text)
 
    driver.quit()

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
    for contain in container:
        currency.append(contain.find_element(By.XPATH, './td[1]').text)
        price.append(contain.find_element(By.XPATH, './td[2]').text)
        percentage_change.append(contain.find_element(By.XPATH, './td[4]').text)
        weekly.append(contain.find_element(By.XPATH, './td[5]').text)
        monthly.append(contain.find_element(By.XPATH, './td[6]').text)
        yoy.append(contain.find_element(By.XPATH, './td[7]').text)
        marketcap.append(contain.find_element(By.XPATH, './td[8]').text)
 
    driver.quit()

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

    for contain in container:
        company_name.append(contain.find_element(By.XPATH,'./td[2]').text)
        eps.append(contain.find_element(By.XPATH,'./td[3]').text)
        consensus.append(contain.find_element(By.XPATH,'./td[4]').text)
        previous.append(contain.find_element(By.XPATH,'./td[5]').text)
        revenue.append(contain.find_element(By.XPATH,'./td[6]').text)
        forecast.append(contain.find_element(By.XPATH,'./td[7]').text)
        marketcap.append(contain.find_element(By.XPATH,'./td[9]').text)
        fiscal.append(contain.find_element(By.XPATH,'./td[10]').text)
    driver.quit()

    data = pd.DataFrame({"company_name":company_name,
                        "eps":eps,
                        "consensus":consensus,
                        "previous":previous,
                        "revenue":revenue,
                        "forecast":forecast,
                        "marketcap":marketcap,
                        "fiscal":fiscal})
    return data       
