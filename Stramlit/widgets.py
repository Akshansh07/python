import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name:")


age=st.slider("Select your age: ", 0, 100, 25)

st.write(f"Your age is: {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected {choice}.")


if name:
    st.write(f"Hello, {name}!")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is  not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


