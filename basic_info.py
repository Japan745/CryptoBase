import streamlit as st

import bit_info
import eth_info
import xlm_info


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
