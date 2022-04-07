import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
from datetime import datetime
import time
import requests
from streamlit_lottie import st_lottie_spinner
import ada
import bch
import bit
import doge
import dot
import eth
import ltc
import shib
import usdt
import xlm


def get_prediction():

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets3.lottiefiles.com/private_files/lf30_h4qnjuax.json"
    lottie_json = load_lottieurl(lottie_url)

    st.warning(
        "NOTE :-  The Predicted values of cryptocurrencies are forecasted by machine learning algorithm and are for your reference so it doesn't guarantee future exact values."
        "Please do a research before taking any further decision based on this forecasted values.")

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Stellar (XLM)', 'Tether (USDT)', 'Bitcoin Cash (BCH)',
                               'Litecoin (LTC)', 'Polkadot (DOT)', 'Dogecoin (DOGE)', 'Cardano (ADA)', 'Shiba Inu (SHIB)'])
        submit_button = st.form_submit_button(label='Submit')
    st.info("FYI : If you want customized forecasting like ( 3 months, 1 year, etc). Please email us by visiting contact us "
            "page. Thank you.")
    if submit_button:
        if crypto == "Bitcoin (BTC)":
            with st_lottie_spinner(lottie_json):
                bit.get_bit()
        if crypto == "Ethereum (ETH)":
            with st_lottie_spinner(lottie_json):
                eth.get_eth()
        if crypto == "Stellar (XLM)":
            with st_lottie_spinner(lottie_json):
                xlm.get_xlm()
        if crypto == "Tether (USDT)":
            with st_lottie_spinner(lottie_json):
                usdt.get_usdt()
        if crypto == "Bitcoin Cash (BCH)":
            with st_lottie_spinner(lottie_json):
                bch.get_bch()
        if crypto == "Litecoin (LTC)":
            with st_lottie_spinner(lottie_json):
                ltc.get_ltc()
        if crypto == "Polkadot (DOT)":
            with st_lottie_spinner(lottie_json):
                dot.get_dot()
        if crypto == "Dogecoin (DOGE)":
            with st_lottie_spinner(lottie_json):
                doge.get_doge()
        if crypto == "Cardano (ADA)":
            with st_lottie_spinner(lottie_json):
                ada.get_ada()
        if crypto == "Shiba Inu (SHIB)":
            with st_lottie_spinner(lottie_json):
                shib.get_shib()

