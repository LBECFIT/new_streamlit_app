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


	################################################################

		with table_new_drop_dataset:

			fig_table_2 = make_subplots(
			    rows=1, cols=2,
			    shared_xaxes=True,
			    horizontal_spacing=0.1,
			    specs=[[{"type": "table"},{"type": "table"}]],
			    subplot_titles=['Newcomers', 'Droppers']

			)

			fig_table_2.add_trace(
			    go.Table(
			        header=dict(
			            values=['<b> User</b>','<b> Regarding</b>'],
			            line_color='darkslategray',
			            fill_color='darkgrey',
			            align=['left','center'],
			            font=dict(color='white', size=11)),
			        cells=dict(
			            values=[
			            [' ']+new_companies_from_this_week+new_weight_from_this_week+new_cover_users_from_this_week,
			            [' ']+['both' for i in range(len(new_companies_from_this_week))]+['weight' for i in range(len(new_weight_from_this_week))]+['covers' for i in range(len(new_cover_users_from_this_week))]],
			            line_color='darkslategray',
			    # 2-D list of colors for alternating rows
			            fill_color = [['white']+['lightblue' for i in range(len(new_companies_from_this_week))]+['#7EDBB4' for i in range(len(new_weight_from_this_week)) ]+['#88C87E' for i in range(len(new_cover_users_from_this_week))]*2],
			            align = ['left', 'center'],
			            font = dict(color = 'darkslategray', size = 12)
			        )
			    ),
			    row = 1,col = 1
			)

			fig_table_2.add_trace(
			    go.Table(
			        header=dict(
			            values=['<b> User</b>','<b> Regarding</b>'],
			            line_color='darkslategray',
			            fill_color='darkgrey',
			            align=['center','center'],
			            font=dict(color='white', size=11)
			        ),
			        cells=dict(
			            values=[[' ']+companies_becoming_inactives+weight_becoming_inactives+covers_users_becoming_inactives,
			                [' ']+['both' for i in range(len(companies_becoming_inactives))]+['weight' for i in range(len(weight_becoming_inactives))]+['covers' for i in range(len(covers_users_becoming_inactives))]
			            ],
			            line_color='darkslategray',
			    # 2-D list of colors for alternating rows
			            fill_color = [['white']+['#EB7C7C' for i in range(len(companies_becoming_inactives))]+['#F1C300' for i in range(len(weight_becoming_inactives)) ]+['#E69214' for i in range(len(covers_users_becoming_inactives))]*2],
			            align = ['left', 'center'],
			            font = dict(color = 'darkslategray', size = 12)
			        )
			    ),
			    row = 1,col = 2
			)

			fig_table_2.update_layout(title_text='Name of droppers and newcomers')
			st.plotly_chart(fig_table_2,use_container_width=True)
