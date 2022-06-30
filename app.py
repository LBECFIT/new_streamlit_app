import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import date, datetime, timedelta
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px
from streamlit_option_menu import option_menu


from waste_graph_functions import *
from list_weekly_kpis import *
from impact_report_metrics import *


st.title('New test app')


header = st.container()
waste_dataset = st.container()
covers_dataset = st.container()
heatmap_dataset = st.container()
model_training = st.container()

inactive_dataset = st.container()
table_new_drop_dataset = st.container()
kpi_dataset = st.container()
fig_bar_dataset = st.container()
fig_pie_dataset = st.container()
line_chart_input_dataset = st.container()

box_plot_dataset = st.container()

individual_heatmap_dataset = st.container()

impact_report_metrics_dataset = st.container()





with st.sidebar:
	selected = option_menu(
		menu_title = 'Menu',
		options = ["Activity Tracker","Weekly KPIs","Outstanding data","Missing data","Impact Report"],
	)


################################################################
################################################################
################################################################

	if selected == 'Weekly KPIs':

		with inactive_dataset:


			headerColor = 'royalblue'
			rowEvenColor = 'paleturquoise'
			rowOddColor = 'white'


			fig_table = go.Figure(data=[go.Table(
			    header=dict(values=['id_company','kitchen','status'],
					fill_color='paleturquoise',
					align='left'),
			    cells=dict(values=[fit_inactive_this_month['id_company'], fit_inactive_this_month['kitchen'], fit_inactive_this_month['Current Type']],
				       fill_color='lavender',
				       align='left'))
			])

			fig_table.update_layout(title_text='Inactive users from last month')

			st.plotly_chart(fig_table,use_container_width=True)
