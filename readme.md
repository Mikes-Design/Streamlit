This is a guide on streamlit

pip intall streamlit 

create folders for data and one called main

create python file called main.py inside the main folder and 

add: 

import streamlit as st

#prints hello world
st.write("Hello World")
#creates an input
st.text_input("Favourite Movie?")

you can assign varriables and functions to st.write

run command line: streamlit run main/main.py

run main.py

add:

is_clicked = st.button("Click Me")

Use normal markdown formating in your string

import pandas as pd

add:

data = pd.read_csv("data.csv")

st.write(data)

import numpy as np

add:

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)

view: https://docs.streamlit.io/ for more methods

create multipage applications by having a directory named pages with each page as a file

main/
    pages/
        1_profile.py
        2_dashboard.py

add to 1_profile.py:

import streamlit as st

st.write("# Profile")

add to 2_dashboard.py:

import streamlit as st

st.write("# Dashboard")



for linking add:

st.link_button("Profile", url="/profile")

create a file called mortage_calculator.py to main folder

add:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Mortage Repayments Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)
home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)


run command line: streamlit run main/mortage_calculator.py



