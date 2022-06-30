import pandas as pd
import streamlit as st

df = pd.read_csv('df_rf3.csv')

st.title('New test app')
st.dataframe(df)
