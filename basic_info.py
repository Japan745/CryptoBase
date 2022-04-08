import streamlit as st

import ada_info
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
                          ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Stellar (XLM)', 'Tether (USDT)', 'Bitcoin Cash (BCH)',
                               'Litecoin (LTC)', 'Polkadot (DOT)', 'Dogecoin (DOGE)', 'Cardano (ADA)', 'Shiba Inu (SHIB)'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "Bitcoin (BTC)":
            bit_info.get_bit_info()
        if crypto =="Cardano (ADA)":
            ada_info.get_ada_info()
        if crypto == "Ethereum (ETH)":
            eth_info.get_eth_info()
        if crypto == "Stellar (XLM)":
            xlm_info.get_xlm_info()
        if crypto == "Litecoin (LTC)":
            lite_info.get_lite_info()
        if crypto == "Tether (USDT)":
            usdt_info.get_usdt_info()
        if crypto == "Polkadot (DOT)":
            dot_info.get_dot_info()
        if crypto == "Bitcoin Cash (BCH)":
            bch_info.get_bch_info()
        if crypto == "Dogecoin (DOGE)":
            doge_info.get_doge_info()
        if crypto == "Shiba Inu (SHIB)":
            shib_info.get_shib_info()
