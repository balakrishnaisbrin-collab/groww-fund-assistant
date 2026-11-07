import streamlit as st
import os
​st.title("Mutual Fund Assistant")
​query = st.text_input("Ask a question about the funds:")
​if query:
st.write(f"Searching for: {query}")
for file in os.listdir('.'):
if file.endswith('.txt'):
with open(file, 'r') as f:
content = f.read()
if query.lower() in content.lower():
st.subheader(file)
st.write(content)
