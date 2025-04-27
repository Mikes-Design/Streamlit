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
#puts columns side by side
col1, col2 = st.columns(2)
#assigns a variable sets min value and default value
home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)


run command line: streamlit run main/mortage_calculator.py

#calculate the repayments

loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate) / 100 / 12
number_of_payments = loan_term * 12
monthly_payment = {
    loan_amount
    *((monthly_interest_rate) * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments -1)
}

#display the repayments

total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly Repayments", value=f"${monethly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"${total_repayments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

#create a data-frame with the payment schedule

schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12) #calculate the year into the loan
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,

        ]
    )

df = pd.DataFrame(
    schedule,
    columns=[
        "Month",
        "Payment",
        "Principal",
        "Interest",
        "Remaining Balance",
        "Year"
    ]
)

#display the data-frame as a chart
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)

make a requirements.txt with:

streamlit>=1.32.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.8.0

