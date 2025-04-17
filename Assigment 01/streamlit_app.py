import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.write("This is a simple data table:")

data = {
    "Name": ["Ali", "Bilal", "Chaudhry"],
    "Age": [25, 30, 35],
    "City": ["Lahore", "Karachi", "Islamabad"]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.button("Click Me")