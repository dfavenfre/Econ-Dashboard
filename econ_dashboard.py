# packages
import streamlit as st
from datetime import datetime
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
            <li> Stay ahead of the market with an advanced sentiment classifier, which accurately evaluates the sentiment of economic/financial commentary, reports, and social media posts.</li>
            <li> Make better-informed investment decisions with powerful LSTM model, leveraging deep learning technology for enhanced Time-Series forecasting</li>
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
selected_date = st.sidebar.date_input("Select A Date", 
                  value=datetime.today().date(),
                  min_value=datetime(2000, 1, 1).date(),
                  max_value=datetime.today().date())
selected_timeframe = st.sidebar.selectbox("Select A Time Frame",
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
    Access a professional-grade calendar featuring daily updates on Metals, Forex, Energy, and Crypto markets, including comprehensive news, actual, forecast, and previous announcements. Customize your experience by filtering currencies and events to focus on what matters most to you.
    """
)
data_option = st.selectbox("Select The Calendar", ["Forex","Metals","Energy", "Crypto"])

def fx_calendar():
    
    economic_calendar = "https://www.forexfactory.com/calendar?day=today"
    driver = uc.Chrome(use_subprocess=True)
    driver.get(economic_calendar)
    
    table_data = driver.find_element(By.XPATH,'//table[@class="calendar__table  "]')
    container = table_data.find_elements(By.XPATH,'//tr[@data-touchable]')

    event_time=[]
    currency_names=[]
    event_names=[]
    actual_data=[]
    forecast_data=[]
    previous_data=[]

    # scraping
    for contain in container:
        event_time.append(contain.find_element(By.XPATH,".//td[@class='calendar__cell calendar__time time']").text)
        currency_names.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__currency currency "]').text)      
        event_names.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__event event"]').text)      
        actual_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__actual actual"]').text)      
        forecast_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__forecast forecast"]').text)   
        previous_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__previous previous"]').text)
           
    driver.quit()
    data = pd.DataFrame({"Time":event_time,"Currency":currency_names,
                                     "Event":event_names,"Actual":actual_data,
                                     "Forecast":forecast_data,"Previous":previous_data})

    
    return data

def metals_calendar():
    economic_calendar = "https://www.metalsmine.com/calendar?day=today"
    driver = uc.Chrome(use_subprocess=True)
    driver.get(economic_calendar)
    
    table_data = driver.find_element(By.XPATH,'//table[@class="calendar__table calendar__table--no-currency "]')
    container = table_data.find_elements(By.XPATH,'//tr[@data-touchable]')

    event_time=[]
    event_names=[]
    actual_data=[]
    forecast_data=[]
    previous_data=[]

    # scraping
    for contain in container:
        event_time.append(contain.find_element(By.XPATH,".//td[@class='calendar__cell calendar__time time']").text)     
        event_names.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__event event"]').text)      
        actual_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__actual actual"]').text)      
        forecast_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__forecast forecast"]').text)   
        previous_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__previous previous"]').text)
           
    driver.quit()
    data = pd.DataFrame({"Time":event_time,
                                     "Event":event_names,"Actual":actual_data,
                                     "Forecast":forecast_data,"Previous":previous_data})
    return data

def energy_calendar():
    economic_calendar = "https://www.energyexch.com/calendar?day=today"
    driver = uc.Chrome(use_subprocess=True)
    driver.get(economic_calendar)
    
    table_data = driver.find_element(By.XPATH,'//table[@class="calendar__table calendar__table--no-currency "]')
    container = table_data.find_elements(By.XPATH,'//tr[@data-touchable]')

    event_time=[]
    event_names=[]
    actual_data=[]
    forecast_data=[]
    previous_data=[]

    # scraping
    for contain in container:
        event_time.append(contain.find_element(By.XPATH,".//td[@class='calendar__cell calendar__time time']").text)
        event_names.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__event event"]').text)      
        actual_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__actual actual"]').text)      
        forecast_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__forecast forecast"]').text)   
        previous_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__previous previous"]').text)
           
    driver.quit()
    data = pd.DataFrame({"Time":event_time,
                                     "Event":event_names,"Actual":actual_data,
                                     "Forecast":forecast_data,"Previous":previous_data})
    return data

def crypto_calendar():
    economic_calendar = "https://www.cryptocraft.com/calendar?day=today"
    driver = uc.Chrome(use_subprocess=True)
    driver.get(economic_calendar)
    
    table_data = driver.find_element(By.XPATH,'//table[@class="calendar__table calendar__table--no-currency "]')
    container = table_data.find_elements(By.XPATH,'//tr[@data-touchable]')

    event_time=[]
    event_names=[]
    actual_data=[]
    forecast_data=[]
    previous_data=[]

    # scraping
    for contain in container:
        event_time.append(contain.find_element(By.XPATH,".//td[@class='calendar__cell calendar__time time']").text)    
        event_names.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__event event"]').text)      
        actual_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__actual actual"]').text)      
        forecast_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__forecast forecast"]').text)   
        previous_data.append(contain.find_element(By.XPATH,'.//td[@class="calendar__cell calendar__previous previous"]').text)
           
    driver.quit()
    data = pd.DataFrame({"Time":event_time,
                                     "Event":event_names,"Actual":actual_data,
                                     "Forecast":forecast_data,"Previous":previous_data})
    return data
  
  # Download Button For Economic Calendar
def convert_df(df):
    return df.to_csv().encode('utf-8')

if data_option == "Forex":
    if st.button("Get Data"):
        calendar_data = fx_calendar()
        st.dataframe(calendar_data, width=800)
if data_option == "Metals":
    if st.button("Get Data"):
        calendar_data = metals_calendar()
        st.dataframe(calendar_data, width=800)   
if data_option == "Energy":
    if st.button("Get Data"):
        calendar_data = energy_calendar()
        st.dataframe(calendar_data, width=800)  
if data_option == "Crypto":
    if st.button("Get Data"):
        calendar_data = crypto_calendar()
        st.dataframe(calendar_data, width=800)  

        
## Sentiment Analysis
st.title("Sentiment Analysis")
st.write(
    """
    Example Of Usage: 
        
        Prompt: 
        "The European auto industry is committed to further reducing emissions," ACEA Director General Sigrid de Vries said in a statement. 
        "However, the Euro 7 proposal is simply not the right way to do this, as it would have an extremely low environmental impact at an extremely high cost."

        Output: 
        Negative : [Probability: 78%]  
        
    """)
model = from_pretrained_keras("dfavenfre/model_use")

# Function to make prediction on new text
def predict_sentiment(text):
    # Make prediction
    prediction = tf.squeeze(model.predict([text]))
    return prediction

def get_sentiment_label(pred):
    sentiment_label = ["Negative", "Neutral", "Positive"]
    max_index = pred.argmax()
    return sentiment_label[max_index]

text_input = st.text_area("Enter the text:", value='')
submit_button = st.button("Predict")

if submit_button and text_input:
    # Make prediction
    prediction = predict_sentiment(text_input)
    sentiment_label = get_sentiment_label(prediction)
    confidence = prediction.max() * 100

    # Output the result
    output = f"{sentiment_label.capitalize()} : [Confidence: {confidence:.2f}%]"
    st.write("Sentiment Prediction:", output)
