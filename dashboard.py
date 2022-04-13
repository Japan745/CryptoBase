import contactus
import About_us
import basic_info
import home
import trading_tips
import live_pricing
import prediction
import streamlit as st
from streamlit_option_menu import option_menu
from  PIL import Image

st.set_page_config(
    page_title="CryptoBase",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto",)

st.markdown("<center><h1 Style=\"overflow: visible; padding-bottom: 50px; padding-top: 0px;\">CryptoBase </h1></center>", unsafe_allow_html=True)
#st.caption("v 1.0.0")
selected = option_menu(
        menu_title=None,
        options=["Home", "Live pricing", "Basic Info", "Prediction", "Trading tips","About Us","Contact us"],
        icons=['house', 'activity', 'info', 'book','app-indicator','person lines fill','mailbox'],
        default_index=0,
        orientation = "horizontal",
        styles={
        "container": {"padding": "5!important", "background-color": "white"},
        "icon": {"color": "#2ECC71", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "light-grey"},
        "nav-link-selected": {"background-color": "#2ECC71"},
}
)

if selected == "Home":
    home.get_home()
elif selected == "Live pricing":
    live_pricing.live_price()
elif selected == "Basic Info":
    basic_info.get_basic_info()
elif selected == "Prediction":
    prediction.get_prediction()
elif selected == "Trading tips":
    trading_tips.trading_tips()
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