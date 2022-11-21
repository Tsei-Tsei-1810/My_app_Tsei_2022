# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st 

st.title('初めてのstreamlit')
st.write('これから作品を作っていきます') 

text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は, ',text,'です')

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション:',condition

option = st.selectbox('好きな数字を教えてください',('1番','2番','3番','4番'))


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    import pandas as pd
import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))