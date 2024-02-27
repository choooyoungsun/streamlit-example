import numpy as np
import pandas as pd
import streamlit as st

st.title('#학년 #반 리포트')

"""
# #학년 #반 리포트
"""
DATE_COLUMN = 'student'
DATA_URL = ('https://docs.google.com/spreadsheets/d/1_BAzpGQQQXzxS8fxrmg9mjTIatv9v9Lx/edit?usp=drive_link&ouid=102505097769871771596&rtpof=true&sd=true')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_student(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
