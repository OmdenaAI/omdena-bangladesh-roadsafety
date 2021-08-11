import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import folium
from folium.plugins import *
from folium import plugins
from streamlit_folium import folium_static
import datetime 
from time import strptime
from datetime import datetime, timedelta
import datetime as dt
import plotly.graph_objects as go
import base64
from pycaret.nlp import *
from plotly.graph_objs import *
import re

import warnings

import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import time

import plotly.figure_factory as ff
import numpy as np

import plotly.express as px
from plotly.graph_objs import *
import sys

from pprint import pprint


def run_and_display_stdout(*cmd_with_args):
    result = subprocess.Popen(cmd_with_args, stdout=subprocess.PIPE)
    for line in iter(lambda: result.stdout.readline(), b""):
        st.text(line.decode("utf-8"))


def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.
    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.
    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')
    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

###########################
# Static Map Daily Observer
###########################

def map_obs():


        map_bd = folium.Map(location= [23.6850, 90.3563], tiles="cartodbpositron", zoom_start = 6)

        # Create a list with lat and long values and add the list to a heat map, then show map
        heat_data = [[row['Latitude'],row['Longitude']] for index, row in df_new.iterrows()]
        HeatMap(heat_data).add_to(map_bd)

        # instantiate a feature group for the incidents in the dataframe
        incidents = folium.map.FeatureGroup()

        # loop through the 100 crimes and add each to the incidents feature group
        for lat, lng, in zip(df_new.Latitude, df_new.Longitude):
            incidents.add_child(
                folium.CircleMarker(
                    [lat, lng],
                    radius=5, # define how big you want the circle markers to be
                    color='darkred',
                    fill=True,
                    fill_color='red',
                    fill_opacity=0.6
                )
            )
        
        #map_van.add_child(incidents)
        folium.TileLayer('cartodbdark_matter').add_to(map_bd)

        # instantiate a mark cluster object for the incidents in the dataframe
        incident = plugins.MarkerCluster().add_to(map_bd)

        # loop through the dataframe and add each data point to the mark cluster
        for lat, lng, label, in zip(df_new.Latitude, df_new.Longitude, df_new.Location_appox):
            folium.Marker(
                location=[lat, lng],
                icon=None,
                popup=label,
            ).add_to(incident)

        # add incidents to map
        map_bd.add_child(incident)
                    
        return map_bd 

###########################
# Static Map Dhaka Tribune
###########################

def map_(df_new):


    map_bd = folium.Map(location= [23.6850, 90.3563], tiles="cartodbpositron", zoom_start = 6)

    # Create a list with lat and long values and add the list to a heat map, then show map
    heat_data = [[row['Latitude'],row['Longitude']] for index, row in df_new.iterrows()]
    HeatMap(heat_data).add_to(map_bd)

    # instantiate a feature group for the incidents in the dataframe
    incidents = folium.map.FeatureGroup()

    # loop through the 100 crimes and add each to the incidents feature group
    for lat, lng, in zip(df_new.Latitude, df_new.Longitude):
        incidents.add_child(
            folium.CircleMarker(
                [lat, lng],
                radius=5, # define how big you want the circle markers to be
                color='darkred',
                fill=True,
                fill_color='red',
                fill_opacity=0.6
            )
        )
    
    #map_van.add_child(incidents)
    folium.TileLayer('cartodbdark_matter').add_to(map_bd)

    # instantiate a mark cluster object for the incidents in the dataframe
    incident = plugins.MarkerCluster().add_to(map_bd)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(df_new.Latitude, df_new.Longitude, df_new.Location_appox):
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(incident)

    # add incidents to map
    map_bd.add_child(incident)
    return map_bd

###########################
# TS Plots using Plotly
###########################

def plot_comparison(loss, val_loss, x, xx, z, zz, model_name):
    
               
        l = list(range(len(loss)))
        ll = list(range(len(val_loss)))
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=l,
            y=loss,
            name = 'Training Loss', line=dict(color='salmon', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=ll,
            y=val_loss,
            name='Validation Loss', line=dict(color='lightseagreen', width=4,
                                      dash='dot')
        ))

        fig.update_layout(title='Model Performance: Loss vs Epochs',
                           xaxis_title='Epochs',
                           yaxis_title='MAE', template="ggplot2")

        fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)


        st.plotly_chart(fig, use_container_width=True)

        #-------------------------------------------------

        ll = list(x.reset_index().Date.astype(str).values)
        lll = list(xx.reset_index().Date.astype(str).values)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=ll,
            y=x,
            name = 'Actual Death Count', line=dict(color='salmon', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=lll,
            y=xx,
            name='Prediction', line=dict(color='lightseagreen', width=4,
                                      dash='dot')
        ))

        fig.update_layout(title='Comparison between Actual & Prediction (Training Set)',
                           xaxis_title='Dates',
                           yaxis_title='Number of Death', template="ggplot2")

        fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)


        st.plotly_chart(fig, use_container_width=True)

        # -----------------------------------------------      
        

        oo = list(z.reset_index().Date.astype(str).values)
        ooo = list(zz.reset_index().Date.astype(str).values)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=oo,
            y=z,
            name = 'Actual Death Count', line=dict(color='salmon', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=ooo,
            y=zz,
            name='Prediction', line=dict(color='lightseagreen', width=2,
                                      dash='dot')
        ))

        fig.update_layout(title='Comparison between Actual & Prediction (Forecast)',
                           xaxis_title='Dates',
                           yaxis_title='Number of Death', template="ggplot2")

        fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)


        st.plotly_chart(fig, use_container_width=True)


##################
# Set up sidebar #
##################

#st.sidebar.markdown('Road safety is a major concern in Bangladesh. Some AI-based initiatives have been made to collect the right datasets, bring insights from the collected data, forecast the number of people killed due to road crashes, and building an object tracking model to compute the velocity of vehicles.')

st.sidebar.image("wc (2).png", use_column_width=True)

option = st.sidebar.selectbox('Select from below', ( "Summary of Statistics", "Geographic Heatmaps", "Time-Series Solutions"))


###################
# Set up main app #
###################

st.markdown("<h1 style='text-align: center; color: white;'>AI for Improving Road Safety in Bangladesh</h1>", unsafe_allow_html=True)



if option == "Summary of Statistics":





    #st.text('Road safety is a major concern in Bangladesh. An estimate states that 55 people are killed in road crashes every day, and that vulnerable road users including walkers, motorcyclists, and unsafe and informal public transportation users account for more than 80% of road traffic deaths [1] . As a direct consequence of rapid growth in population, motorization and urbanization, the situation is deteriorating rapidly. The potential of maturing Artificial Intelligence (AI) and Internet-of-Things (IoT) technologies to enable rapid improvements in road safety has been largely overlooked. There is a pressing need and opportunity to improve road safety by enacting effective and coordinated Artificial Intelligence-driven (AI) policies and actions, which will necessitate significant improvements in the relevant sectors, such as better enforcement, better roads including improving design to eliminate accident black spots, and improved public education programs.')
    #st.markdown('Road safety is a major concern in Bangladesh. Some AI-based initiatives have been made to collect the right datasets, bring insights from the collected data, forecast the number of people killed due to road crashes, and building an object tracking model to compute the velocity of vehicles.')
    st.markdown("<p style='text-align: center; color: white;'>Road safety is a major concern in Bangladesh. Some AI-based initiatives have been made to collect the right datasets, bring insights from the collected data, forecast the number of people killed due to road crashes, and building an object tracking model to compute the velocity of vehicles. </p>", unsafe_allow_html=True)
    # bootstrap 4 collapse example
    st.subheader("Analysis & Visualization of Prothom Alo Datasets")
    components.html(
        """
        <div class="flourish-embed flourish-chart" data-src="visualisation/6977552"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
        """,
        height=700,
    )
    components.html(
        """
        <div class="flourish-embed" data-src="story/921147"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
        """, height=850,
    )


# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------ Summary of Statistics ends here
# --------------------------------------------------------------------------------------------------------------------------------------------------

      
if option == "Time-Series Solutions":
    sol_type = st.radio("Select from below", ("Prediction of Number of Death from Road Accidents", "Prediction of Chances of Death Caused by Road Accidents"))

    if sol_type == "Prediction of Number of Death from Road Accidents":

        st.subheader('Time-Series Forecast with LSTM')

        df = pd.read_csv('Dhaka_Tribune_TS.csv')
        df['Period'] = pd.to_datetime(df['Period'])
        df["Date"] = df['Period'].dt.date

        df = df[['Date', 'Deaths']]

        start_ = df.Date.max()
        end_ = df.Date.min()

        test_end = df.Date.max()
        test_start = df.Date.max() - timedelta(days = 60)

        train_end = test_start - timedelta(days = 1)
        train_start = train_end - timedelta(days = 365*5)
      
        st.text(' ')
        st.text('Training Period: `%s` to `%s`' % (end_, train_end))
        st.text('Forecast Period: `%s` to `%s`' % (test_start, test_end))

        
        comparison = pd.read_csv('forecast.csv')
        st.subheader('Prediction on the Test Dataset')
        st.write(comparison)
        tmp_download_link = download_link(comparison, 'comparison.csv', 'Click here to download as CSV')
        st.markdown(tmp_download_link, unsafe_allow_html=True)

        def plot_comparison(x, xx):
    
            ll = list(x.index.astype(str).values)
            lll = list(xx.index.astype(str).values)

            fig = go.Figure()

            fig.add_trace(go.Scatter(x=ll, y=x, name = 'Actual Death Count', line=dict(color='salmon', width=2)))
            fig.add_trace(go.Scatter(x=lll, y=xx, name='Prediction', line=dict(color='lightseagreen', width=4, dash='dot')))
            fig.update_layout(title='Comparison of Actual Death Count & Prediction (Test Set)',
                               xaxis_title='Dates', yaxis_title='Number of Death', template="ggplot2")
            fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
            st.plotly_chart(fig, use_container_width=True)
        
        plot_comparison(comparison['Actual Death Count'], comparison['Prediction'])

        comparison_train = pd.read_csv('prediction_on_training.csv')
        st.subheader('Prediction on the Training Dataset')
        st.write(comparison_train)
        tmp_download_link = download_link(comparison_train, 'comparison_train.csv', 'Click here to download as CSV')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
        comparison_train = comparison_train.set_index('Date')

        def plot_comparison(x, xx):
    
            ll = list(x.index.astype(str))
            lll = list(xx.index.astype(str))

            fig = go.Figure()

            fig.add_trace(go.Scatter(x=ll, y=x, name = 'Actual Death Count', line=dict(color='salmon', width=2)))
            fig.add_trace(go.Scatter(x=lll, y=xx, name='Prediction', line=dict(color='lightseagreen', width=4, dash='dot')))
            fig.update_layout(title='Comparison of Actual Death Count & Prediction (Training Set)',
                               xaxis_title='Dates', yaxis_title='Number of Death', template="ggplot2")
            fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
            st.plotly_chart(fig, use_container_width=True)
        
        plot_comparison(comparison_train['Actual Death Count'], comparison_train['Prediction'])

        st.subheader('Evaluation Scores on the Test Set')

        st.write(' ')
        st.write('Mean Absolute Error: 2.6250')
        st.write('Mean Squared Error: 14.1250')
        st.write('Root Mean Square Error: 3.7583')
        st.write('Mean Absolute Percentage Error: 27.6968')
        st.write('R2 Score: 0.7270')

        st.subheader('More on Data Preprocessing and Model Development')

        st.write('- [Download the saved model](https://github.com/SumaiaParveen/Road-Accident-TS-Analysis/blob/main/weights.h5)')
        st.write('- [See the notebook](https://github.com/SumaiaParveen/Road-Accident-TS-Analysis/blob/main/LSTM%20TS%20Forecast.ipynb)')


# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------- Time Series Forecast ends here
# --------------------------------------------------------------------------------------------------------------------------------------------------
    if sol_type == "Prediction of Chances of Death Caused by Road Accidents":

        st.subheader('Time-Series Classification with Quadratic Discriminant Analysis')

        df = pd.read_csv('Dhaka_Tribune_TS.csv')
        df['Period'] = pd.to_datetime(df['Period'])
        df["Date"] = df['Period'].dt.date

        df = df[['Date', 'Deaths']]

        start_ = df['Date'].max()
        end_ = df['Date'].min()

        test_end = df['Date'].max() - timedelta(days = 1)
        test_start = df['Date'].max() - timedelta(days = 90) - timedelta(days = 1)

        train_end = test_start - timedelta(days = 1)
        train_start = train_end - timedelta(days = 90*8)
              
        st.text(' ')
        st.text('Training Period: `%s` to `%s`' % (train_start, train_end))
        st.text('Forecast Period: `%s` to `%s`' % (test_start, test_end))

        test = pd.read_csv('test_results.csv')
        st.subheader('Prediction on the Test Dataset')
        st.write(test)
        tmp_download_link = download_link(test, 'final_results.csv', 'Click here to download as CSV')
        st.markdown(tmp_download_link, unsafe_allow_html=True)

        act = pd.read_csv('actuals.csv')
        pred = pd.read_csv('prediction.csv')

        import plotly.graph_objects as go
        import pandas as pd


        fig = go.Figure(data=go.Scatter(x=act['Date'],
                                        y=act['Death?'],
                                        mode='lines+markers',
                                        marker=dict(
                                            size=12,
                                            color='LightSkyBlue'),
                                        text=act['Death?'], opacity = 0.9)) # hover text goes here

        fig.update_layout(title='Actual Death Data: 2021/03/29 to 2021/06/26',  xaxis=dict(showgrid=False, title="Date"), yaxis=dict(showgrid=False, title="Death?"))
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure(data=go.Scatter(x=pred['Date'],
                                        y=pred['Death?'],
                                        mode='lines+markers',
                                        marker=dict(
                                            size=12,
                                            color='MediumSeaGreen'),
                                        text=pred['Death?'], opacity = 0.9)) # hover text goes here

        fig.update_layout(title='Predicted Results: 2021/03/29 to 2021/06/26', xaxis=dict(showgrid=False, title="Date"), yaxis=dict(showgrid=False, title="Death?"))
        st.plotly_chart(fig, use_container_width=True)

        st.subheader('Evaluation Scores on the Test Set')

        st.info('True Positives: 16, False Positives: 21, True Negatives: 40, False Negatives: 13')

        st.write('Accuracy Score: 0.6222')
        st.write('Macro Average of Recall Score: 0.6037')
        st.write('Weighted Average of Recall Score: 0.6222')
        st.write('Macro Average of Precision Score: 0.5936')
        st.write('Weighted Average of Precision Score: 0.6509')
        st.write('Macro Average of F1 Score: 0.5933')
        st.write('Weighted Average of F1 Score: 0.6319')


        st.subheader('More on Data Preprocessing and Model Development')

        st.write('- [See the notebook](https://nbviewer.jupyter.org/github/SumaiaParveen/Road-Accident-TS-Analysis/blob/main/QDA%20for%20Road%20Accident%20TS%20Classification.ipynb)')



# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------- Time Series Classification ends here
# --------------------------------------------------------------------------------------------------------------------------------------------------


if option == "Geographic Heatmaps":
    news_type = st.radio("Newspaper Selection", ("Dhaka Tribune", "Daily Observer"))
    if news_type == "Dhaka Tribune":

        df = pd.read_csv('Dhaka_Tribune_hm.csv')
        df_new = df.copy()

        df_new = df_new.dropna()
        folium_static(map_(df_new))

        df_new["Weight"] = df_new['Accident date'].astype(str)
        df_new["Weight"] = df_new["Weight"].str[5:7]
        df_new["Weight"] = df_new["Weight"].astype(float)
        
        
        df_new['year'] = pd.DatetimeIndex(df_new['Accident date']).year
        df_new['month'] = pd.DatetimeIndex(df_new['Accident date']).month

        import datetime
        lista_tempo = [] 

        for x in df_new['month']: 
            monthinteger = x 
            lista_tempo.append(datetime.date(1900, monthinteger, 1).strftime('%B')) 
    
        df_new['months_in_full'] = lista_tempo 
        df_new['month_year'] = [d.split('-')[1] + " " + d.split('-')[0] for d in df_new['Accident date'].astype(str)]

        df_new['indexx'] = df_new['months_in_full'] + ' ' + df_new['year'].astype(str)
        lista_index = df_new['indexx'].unique().tolist()

        weight_list = []

        df_new['conta'] = 1 
        for x in df_new['month_year'].sort_values().unique(): 
            weight_list.append(df_new.loc[df_new['month_year'] == x, 
                                                ['Latitude',"Longitude",'conta']].groupby(['Latitude','Longitude']).sum().reset_index().values.tolist()) 

            
        base_map = folium.Map(location=[23.6850, 90.3563],tiles="stamen toner",zoom_start = 6) 

        #create the heatmap from our List 
        HeatMapWithTime(weight_list, radius=15,index= lista_index, gradient={0.1: 'blue',0.25: 'green', 0.25: 'yellow', 0.95: 'orange', 1: 'red'}, \
                                                                             
                                auto_play =True, min_opacity=0.5, max_opacity=1, use_local_extrema=True).add_to(base_map) 
                                                                        
                                                                             
        folium_static(base_map)

    if news_type == "Daily Observer":
        df = pd.read_csv('Daily_Observer_hm.csv')
        df_new = df.copy()
        df_new = df_new.dropna()
        folium_static(map_obs())

        df_new['month'] = df_new.date.str[3:6]
        month_num = []
        for i in range(len(df_new)):
            month_num.append(strptime(df_new['month'][i],'%b').tm_mon)
        df_new['month_num'] = month_num
        df_new["Weight"] = df_new['month_num'].astype(float)    

        import datetime
        lista_tempo = [] 

        for x in df_new['month_num']: 
            monthinteger = x 
            lista_tempo.append(datetime.date(1900, monthinteger, 1).strftime('%B')) 
    
        df_new['months_in_full'] = lista_tempo 
        df_new['month_year'] = df_new['month'] + ' ' + df_new['Year'].astype(str)   

        df_new['indexx'] = df_new['month'] + ' ' + df_new['Year'].astype(str)
        lista_index = df_new['indexx'].unique().tolist()

        weight_list = []

        df_new['conta'] = 1 

        for x in df_new['month_year'].sort_values().unique(): 
            weight_list.append(df_new.loc[df_new['month_year'] == x, 
                                        ['Latitude',"Longitude",'conta']].groupby(['Latitude','Longitude']).sum().reset_index().values.tolist())  
    
        base_map = folium.Map(location=[23.6850, 90.3563],tiles="stamen toner",zoom_start = 6) 

        #create the heatmap from our List 
        HeatMapWithTime(weight_list, radius=20,index= lista_index, gradient={0.1: 'blue',0.5: 'green', 0.5: 'yellow', 0.95: 'orange', 1: 'red'}, \
                                                                     
                        auto_play =True, min_opacity=0.5, max_opacity=1, use_local_extrema=True).add_to(base_map) 
                                                                
                                                                     
        folium_static(base_map)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------- Geographic Heatmaps ends here
# --------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------- Text Analytics ends here
# --------------------------------------------------------------------------------------------------------------------------------------------------