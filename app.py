import streamlit as st import os

st.title("Mutual Fund Info")

def read\_txt\_files(): for file in os.listdir("'): if file.endswith('.txt'): with open(file, 'r')

as f:

st.subheader(file) st.text(f.read())

read\_txt\_files()
