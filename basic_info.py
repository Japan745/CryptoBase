import streamlit as st

import bit_info
import eth_info
import xlm_info


def get_basic_info():

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                          ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Stellar (XLM)', 'Tether (USDT)', 'Bitcoin Cash (BCH)',
                               'Litecoin (LTC)', 'Polkadot (DOT)', 'Dogecoin (DOGE)', 'Cardano (ADA)', 'Shiba Inu (SHIB)'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "Bitcoin (BTC)":
            bit_info.get_bit_info()
        if crypto == "Ethereum (ETH)":
            eth_info.get_eth_info()
        if crypto == "Stellar (XLM)":
            xlm_info.get_xlm_info()
