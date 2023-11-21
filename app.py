import streamlit as st
import pandas as pd
from PIL import Image
import time
import json
import random
from datetime import datetime
import datetime
import os
import numpy as np
import requests


from tqdm import tqdm
from cred_here import *

import ast

# Tools

import folium
from shapely.geometry import Polygon
import numpy as np
import geojson
import geopandas as gpd
from tqdm import tqdm
from shapely.geometry import Polygon
import shapely.wkt
from haversine import haversine, Unit
import random
import time
from pyproj import Geod

from shapely import wkt
from geopandas import datasets, GeoDataFrame, read_file, points_from_xy

from folium.plugins import MeasureControl
from folium.plugins import MarkerCluster

from utils import GetLatLon2,cal_dist,distance_estac,transform_df_map,marker_rest
from streamlit_folium import folium_static

image = Image.open('1_Fuel-prices.jpg')

st.sidebar.image(image , caption="Nearby Oil App",width = 256)
app_mode = st.sidebar.selectbox("Choose app mode", ["Run App","About Me"])


if app_mode == 'Run App':

    st.title('Nearby Oil Station App')
    st.markdown('App Description')

    df_map = pd.read_csv('DF_STATIONS.csv')
    cities =  list(df_map['Municipio'].unique())

    c1,c2,c3,c4,c5 = st.columns((1,6,6,6,1))

    choose_city =  c2.selectbox("Choose city", cities)

    central_location = c2.text_input('Central Location', 'CC Multiplaza , Bogotá')

    DEVELOPER_KEY = YOUR_API_KEY

    if len(central_location) != 0 :

        R = GetLatLon2(central_location,YOUR_API_KEY)
        geo_source = R[1],R[2]

        unit = 'Km'
        rad = c4.slider('Radius',1,3,1)

        df_city = df_map[df_map['Municipio']==choose_city]
        df_city.reset_index(inplace = True)
        df_city.drop(columns = 'index',inplace = True)

        df_city =  transform_df_map(df_city)

        results = distance_estac(geo_source,df_city,rad,unit)
        results = results.reset_index()
        results = results.drop(columns = 'index')
        products =  list(results['Producto'].unique())

        gdf_stores_results = GeoDataFrame(results,
                                            geometry=points_from_xy(results.LNG,results.LAT))


        choose_products =  c3.selectbox("Choose Oil", products)

        if c3.button('SHOW MAP'):

            gdf_stores_results2 = gdf_stores_results[gdf_stores_results['Producto']==choose_products]
            gdf_stores_results2 = gdf_stores_results2.reset_index()
            gdf_stores_results2 = gdf_stores_results2.drop(columns = 'index')
            icono = "usd"

            m = folium.Map([geo_source[0],geo_source[1]], zoom_start=15)

            # Circle
            folium.Circle(
            radius=int(rad)*1000,
            location=[geo_source[0],geo_source[1]],
            color='green',
            fill='red').add_to(m)

            # Centroid
            folium.Marker(location=[geo_source[0],geo_source[1]],
                                icon=folium.Icon(color='black', icon_color='white',
                                icon="home", prefix='glyphicon')
                                ,popup = "<b>CENTROID</b>").add_to(m)

            marker_rest(gdf_stores_results2,m,unit,choose_products,icono)

            # call to render Folium map in Streamlit
            folium_static(m)




elif app_mode == "About Me":
    st.title('Nearby Oil Station App')
    st.success("Feel free to contacting me here 👇 ")

    col1,col2,col3,col4 = st.columns((2,1,2,1))
    col1.markdown('* [**LinkedIn**](https://www.linkedin.com/in/kevin-guzman-55815b235/)')
    col1.markdown('* [**GitHub**](https://github.com/KevinGuzm)')
    image2 = Image.open('profile.jpg')
    col3.image(image2,width=230)