from tkinter import Image
from PIL import Image
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
import streamlit as st
from streamlit_option_menu import option_menu
import contactus
import About_us
import basic_info
import home
import trading_tips
import live_pricing
<<<<<<< HEAD
=======
import prediction
base = "dark"
>>>>>>> b7ad90615381c4fe15093a0c6eee59ba0303b01d


base = "dark"
im = Image.open("images/ravi.jpg")
st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="auto",
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an extremely cool app!"
    # }
)


# with st.sidebar:
# st.title('Home')
# st.subheader('Prediction')
#st.subheader('Live price')
# st.subheader('Comparison')
#st.subheader('Crypto Info')
#st.subheader('Contact Us')
selected = option_menu(


    menu_title=None,

    orientation="horizontal",

    options=["Home", "Live pricing", "Basic Info", "Prediction",
             "Trading tips", "About Us", "Contact us"],
    default_index=0
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

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("dashboard")