# Econ-Dashboard
A centralized dashboard for screening and downloading Stock/ETF/FX/Economic Data, as well as viewing Forex, Metal, Energy, and Crypto Calendars. Apart from being a one-stop data provider, Econ-Dashboard is also equipped with sentiment classifier trained on financial/economic sentiment. Time-series forecasting is armed with two LSTM models distinguished for different market capitalization constraints. 

The sentiment classification model is available at my [huggingface](https://huggingface.co/dfavenfre/model_use/tree/main) repository

## Model Implementation
The model is equipped with a pre-trained embedding layer([Universal-Sentence-Encoder](https://tfhub.dev/google/universal-sentence-encoder/4)), therefore, the model deployment requires a customized kerasmodel class. 
```Python
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
    best_use_model = tf.keras.models.load_model(r"WRITE_MODELS_PATH")
```
# Available Features
## Stock Screener
* Stock screener is equipped with yfinance API. You can select time frame and data interval, and download the data
* If you're not sure about which ticker/symbol format, head over to [yahoo finance]([url](https://finance.yahoo.com/)) to check the ticker/symbol 
![image](https://github.com/dfavenfre/Econ-Dashboard/assets/118773869/6d066621-104c-4e7d-8e4c-4e1343ef6cbb)
## Data Provider
* Data Provider is powered with various economic and financial data, including economic calendar, FX , Stock , Earnings, Commodities, Bonds, Crypto market data.
![image](https://github.com/dfavenfre/Econ-Dashboard/assets/118773869/d068d96c-42bb-41e3-aab9-468f05da5ca9)
## Sentiment Analysis
Sentiment Classification model is trained on Phrasebank's agreeall Financial sentiment [dataset](https://huggingface.co/datasets/financial_phrasebank/viewer/sentences_allagree/train).
![image](https://github.com/dfavenfre/Econ-Dashboard/assets/118773869/2c6b9dff-cf15-4ea5-bd00-776fd0854abd)


## Time-Series Forecasting
Forecasting model is a fine-tuned LSTM model that is trained on 7-days look-back period to forecast 1-day forward window value. The model inputs are; last available Volume and 7 consecutive daily close data. You have option to either upload your own data, or write the required data inputs on your own. The time-series feature is armed with two models that are specifically trained for both Large and Small Cap Stocks. You May Select The Model For Your Stock

![image](https://github.com/dfavenfre/Econ-Dashboard/assets/118773869/6c19731e-97d6-44b4-9e3d-4af5036f490f)
