

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io
im = Image.open("images/ravi.jpg")
st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="auto",)


choose = option_menu("Crypto future", ["Home", "Live pricing", "Basic Info", "Prediction", "Trading tips","About Us","Contact us"],
                         icons=['house', 'activity', 'info', 'book','app-indicator','person lines fill','mailbox'],
                         menu_icon="currency-bitcoin", default_index=0, orientation = "horizontal",
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
}
)