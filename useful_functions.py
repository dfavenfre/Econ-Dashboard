import numpy as np
from numpy import ndarray
import streamlit as st
import tensorflow as tf
import pandas as pd

def prepare_timeseries(data, target_column:str, lookback:int)->ndarray:
  """
  Description:
  ------------
  Prepare time series data with provided lookback period. The data will be shifted accordingly the provided lookback, and then NaN cells will be dropped for time series modelling. 
  Parameters:
  ------------
  data(ndarray): The feature data to be used in time-series forecasting model
  target_column(str): The column that will be forecasted
  lookback(int): Number of lookback-periods the model should take into consideration
  Returns:
  ------------
  Returns whole Data (data) prepared in accordance with the provided lookback 
  """
  data = data[["Volume","Close"]]
  data_copy = data.copy()
  for i in range(lookback):
    data_copy[f"target_column+{i+1}"] = data_copy[target_column].shift(periods=i+1)

  X = data_copy.dropna().astype(np.float32)
  
  return X.iloc[-1:,:]

def predict_forward_window(prediction_data:ndarray, model_name):
  """
  Description:
  -----------
  Calculates the potential percentage change between last available close data and the predicted close.
  """
  prediction = tf.squeeze(model_name.predict(prediction_data))
  prediction = prediction.numpy()
  result = (prediction / prediction_data["Close"].values -1 )*100
  
  # Drowdown
  if result<0:
    st.write("Target Price: {:.3f}".format(prediction),"\n",
          "\nPotential Downside: {}".format(str(np.round(result,2))+"%"))

  # Up-ward surge
  else:
    st.write("Target Price: {:.3f}".format(prediction),"\n",
    "\nPotential Upside: {}".format(str(np.round(result,2))+"%"))

st.cache_data()
def upload_data():
    dataframe  = pd.DataFrame(uploaded_file)
    return dataframe
