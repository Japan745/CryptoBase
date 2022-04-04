import streamlit as st
from streamlit_option_menu import option_menu
import contactus
import About_us
import basic_info
import home
import trading_tips
import live_pricing
import prediction

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


selected = option_menu("Crypto future", ["Home", "Live pricing", "Basic Info", "Prediction", "Trading tips","About Us","Contact us"],
                         icons=['house', 'activity', 'info', 'book','app-indicator','person lines fill','mailbox'],
                         menu_icon="currency-bitcoin", default_index=0, orientation = "horizontal",
                         styles={
        "container": {"padding": "5!important", "background-color": "light-grey"},
        "icon": {"color": "#2ECC71", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "light-grey"},
        "nav-link-selected": {"background-color": "#2ECC71"},
}
)

if selected == "Home":
    #home.home()
    st.title("This is home page")
elif selected == "Live pricing":
    live_pricing.live_price()
    #st.title("This is live pricing section")
elif selected == "Basic Info":
    basic_info.get_basic_info()
elif selected == "Prediction":
    prediction.get_prediction()
elif selected == "Trading tips":
    trading_tips.trading_tips()
    #st.title("This is trading tips pAGE")
elif selected == "About Us":
     About_us.aus()
elif selected == "Contact us":
    contactus.callus()

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)