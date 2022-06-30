import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import date, datetime, timedelta
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px

df = pd.read_csv('df_covers_tar.csv')

st.title('New test app')
st.dataframe(df)
