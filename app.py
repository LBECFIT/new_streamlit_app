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

df = pd.read_csv('df_covers.csv')

st.title('New test app')
st.dataframe(df)


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


	if selected == 'Activity Tracker':




		with header:
			st.title('Activity Tracker')



		with waste_dataset:
			focus_company = st.text_input('Group you want to focus on', 'APAC')
			df_rf3 = pd.read_csv('df_rf3.csv',sep=',')
			df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste']).dt.floor('d')
			df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste']).dt.date
			df_rf3 = df_rf3[df_rf3['id_company'].str.startswith(focus_company, na = False)].reset_index()
			weight_by_company_c = df_rf3.copy()
			weight_by_company_c = weight_by_company_c.groupby(['id_company', 'date_waste','shift'])['weight'].sum().reset_index()

			fig = go.Figure()

			name = weight_by_company_c['id_company'].to_list()
			name = list(set(name))
			name2=['BEIGH','NAYRW','TAIGH','SOCAL','BANGH','GUAGH','CJUGH','SERLS']
			L_bf = [True,False,False]
			L_lunch = [False,True,False]
			L_dinner = [False,False,True]
			L_allshifts = [True,True,True]



			dicoi = [dict(label="{}".format(name2[i]),method="update",args=[{"visible": true_false(i,name)},{"title": "{}".format(name[i])}])for i in range(len(name))]




			for i in range(len(name)): 
			    x_bf = weight_by_company_c[(weight_by_company_c['id_company']==name[i])&(weight_by_company_c['shift']=='Breakfast')]['date_waste'].to_list()
			    y_bf = weight_by_company_c[(weight_by_company_c['id_company']==name[i])&(weight_by_company_c['shift']=='Breakfast')]['weight'].to_list()
			    fig.add_trace(go.Bar(x=x_bf, y=y_bf, name=name2[i]+' Breakfast'))

			    x_lunch = weight_by_company_c[(weight_by_company_c['id_company']==name[i])&(weight_by_company_c['shift']=='Lunch')]['date_waste'].to_list()
			    y_lunch = weight_by_company_c[(weight_by_company_c['id_company']==name[i])&(weight_by_company_c['shift']=='Lunch')]['weight'].to_list()
			    fig.add_trace(go.Bar(x=x_lunch, y=y_lunch, name=name2[i]+' Lunch'))

			    x_dinner = weight_by_company_c[(weight_by_company_c['id_company']==name[i])&(weight_by_company_c['shift']=='Dinner')]['date_waste'].to_list()
			    y_dinner = weight_by_company_c[(weight_by_company_c['id_company']==name[i])&(weight_by_company_c['shift']=='Dinner')]['weight'].to_list()
			    fig.add_trace(go.Bar(x=x_dinner, y=y_dinner, name=name2[i]+' Dinner'))
			    #fig.update_layout(barmode='grouped')

			fig.update_layout(title = '{} graph of foodwaste over time (1st version)'.format('APAC'),
			    updatemenus=[
			        dict(
			            active=0,
			            buttons=list([
			                dict(label="Breakfast",
			                     method="update",
			                     args=[{"visible": L_bf*len(name)},
			                           {"title": "{} Breakfast".format('APAC')}]),
			                dict(label="Lunch",
			                     method="update",
			                     args=[{"visible": L_lunch*len(name)},
			                           {"title": "{} Lunch".format('APAC')}]),
			                dict(label="Dinner",
			                     method="update",
			                     args=[{"visible": L_dinner*len(name)},
			                           {"title": "{} Dinner".format('APAC')}]),
			                dict(label="All shifts",
			                     method="update",
			                     args=[{"visible": L_allshifts*len(name)},
			                           {"title": "{} all shifts".format('APAC')}])]+dicoi
			            ),
			        )
			    ],
			    xaxis=dict(
			        rangeselector=dict(
			            buttons=list([
			                dict(count=7,
			                     label="1 weeks",
			                     step="day",
			                     stepmode="backward"),
			                dict(count=14,
			                     label="2 weeks",
			                     step="day",
			                     stepmode="backward"),
			                dict(count=1,
			                     label="month",
			                     step="month",
			                     stepmode="todate"),
			                dict(step="all")
			            ])
			        ),
			        rangeslider=dict(
			            visible=True
			        ),
			        type="date"
			    ))
			fig.update_yaxes(automargin=True)
			fig.update_xaxes(automargin=True)


			st.plotly_chart(fig,use_container_width=True)
