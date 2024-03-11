import time
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
    return df

@st.cache_data
def show_data(data):
    time.sleep(2)  # This makes the function take 2s to run
    return data

df = get_data()
data = df["str"].unique()

st.dataframe(show_data(data))
st.button("Re-run")

#exemplo cache_resource 

@st.cache_resource   # 👈 Turn off copying behavior
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv")
st.dataframe(df)

df.drop(columns=['Lat'], inplace=True)  # 👈 Mutate the dataframe inplace

st.button("Rerun")