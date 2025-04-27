import streamlit as st
import pandas as pd

#prints hello world
st.write("Hello World")
#creates an input
st.text_input("Favourite Movie?")

is_clicked = st.button("Click Me")


data = pd.read_csv("data/whitley_county_uneymployment.csv")

st.write(data)