import streamlit as st
import pandas as pd
import numpy as np

#prints hello world
st.write("Hello World")
#creates an input
st.text_input("Favourite Movie?")

is_clicked = st.button("Click Me")


data = pd.read_csv("data/whitley_county_uneymployment.csv")

st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)