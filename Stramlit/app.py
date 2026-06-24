import streamlit as st
import pandas as pd
import numpy as np


## Title of application
st.title("Hello Streamlit")

## Display a simple text
st.write("This is a simple text.")

## Display a dataframe

df = pd.DataFrame({
    'first column': [1,  2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the data frame

st.write("Hrere is data frame")
st.write(df)

## Display line chart 

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)