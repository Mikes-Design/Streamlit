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



