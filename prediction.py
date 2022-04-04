import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
from datetime import datetime

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

    st.warning(
        "NOTE :-  The Predicted values of cryptocurrencies are forecasted by machine learning algorithm and are for your reference so it doesn't guarantee future exact values."
        "Please do a research before taking any further decision based on this forecasted values.")

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['BTC', 'ETH', 'XLM', 'USDT', 'BCH', 'LTC', 'DOT', 'DOGE', 'ADA', 'SHIB'])
        submit_button = st.form_submit_button(label='Submit')
    st.info("FYI : If you want customized forecasting like ( 3 months, 1 year, etc). Please email us by visiting contact us "
            "page. Thank you.")
    if submit_button:
        if crypto == "BTC":
            bit.get_bit()
        if crypto == "ETH":
            eth.get_eth()
        if crypto == "XLM":
            xlm.get_xlm()
        if crypto == "USDT":
            usdt.get_usdt()
        if crypto == "BCH":
            bch.get_bch()
        if crypto == "LTC":
            ltc.get_ltc()
        if crypto == "DOT":
            dot.get_dot()
        if crypto == "DOGE":
            doge.get_doge()
        if crypto == "ADA":
            ada.get_ada()
        if crypto == "SHIB":
            shib.get_shib()

