import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import date, datetime, timedelta
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px

from waste_graph_functions import *
from streamlit_option_menu import option_menu

from list_weekly_kpis import *

from impact_report_metrics import *

df = pd.read_csv('df_covers.csv')

st.title('New test app')
st.dataframe(df)
