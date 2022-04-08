import streamlit as st

import bit_info
import eth_info
import xlm_info
import lite_info
import usdt_info
import dot_info
import bch_info
import doge_info
import shib_info


def get_basic_info():

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                          ['BTC', 'ETH', 'XLM', 'USDT', 'BCH', 'LTC', 'DOT', 'DOGE', 'ADA', 'SHIB'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "BTC":
            bit_info.get_bit_info()
        if crypto == "ETH":
            eth_info.get_eth_info()
        if crypto == "XLM":
            xlm_info.get_xlm_info()
        if crypto == "LTC":
            lite_info.get_lite_info()
        if crypto == "USDT":
            usdt_info.get_usdt_info()
        if crypto == "DOT":
            dot_info.get_dot_info()
        if crypto == "BCH":
            bch_info.get_bch_info()
        if crypto == "DOGE":
            doge_info.get_doge_info()
        if crypto == "SHIB":
            shib_info.get_shib_info()
