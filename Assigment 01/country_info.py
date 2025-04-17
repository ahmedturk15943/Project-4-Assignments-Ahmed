import streamlit as st
import requests

st.title("Country Information")

country = st.text_input("Enter country name:")
if country:
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    if response.status_code == 200:
        data = response.json()[0]
        st.write(f"Capital: {data['capital'][0]}")
        st.write(f"Population: {data['population']}")
        st.write(f"Currency: {list(data['currencies'].keys())[0]}")
    else:
        st.error("Country not found!")