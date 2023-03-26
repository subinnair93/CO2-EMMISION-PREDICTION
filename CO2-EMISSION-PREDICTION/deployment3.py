

import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
 
from statsmodels.tsa.holtwinters import Holt

import base64

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("C:\\Users\\91813\\nithin ppt\\Clean Data.csv",header=0,index_col=0,parse_dates=True)

model=Holt(df["CO2"]).fit()

st.title("Forecasting CO2 Emission ")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('co2.png')

choice= st.radio("Menu",["Objective","Prediction"])

if choice == "Objective":
    st.subheader("Business Objective")
    st.write("To forecast Co2 levels for an organization so that the organization can follow government norms with respect to Co2 emission levels")
    
elif choice == "Prediction":
    year = st.slider("Select your year ",2015,2100,step=1)
    st.subheader("Select your year and press Predict")
    pred= model.forecast(year)
    
    if st.button("Predict"):
        st.subheader("Your prediction")
        pred
        
        st.subheader("Line plot of the predicted data")
        plt.figure(figsize=(20,20))
        plt.xlabel('CO2')
        plt.ylabel('Year')
        plt.title('Forecasting')
        plt.grid(True)
        st.line_chart(pred)
        
             
