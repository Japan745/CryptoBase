import streamlit as st
import pandas as pd
import cryptocompare
import datetime
import time


def live_price():

    def get_crypto_price(cryptocurrency, currency):
        return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

    def animate(i,crypto):

        df2 = pd.DataFrame([get_crypto_price(crypto, 'CAD')], index=[datetime.datetime.now()],columns=[' '])

        my_chart.add_rows(df2)

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['BTC', 'ETH', 'XLM', 'USDT', 'BCH', 'LTC', 'DOT', 'DOGE', 'ADA', 'SHIB'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "BTC":
            df1 = pd.DataFrame([get_crypto_price('BTC', 'CAD')], index=[datetime.datetime.now()], columns=['Bitcoin (CAD)'])


            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "ETH":
            df1 = pd.DataFrame([get_crypto_price('ETH', 'CAD')], index=[datetime.datetime.now()],
                               columns=['Ethereum (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "XLM":
            df1 = pd.DataFrame([get_crypto_price('XLM', 'CAD')], index=[datetime.datetime.now()],
                               columns=['XLM (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "USDT":
            df1 = pd.DataFrame([get_crypto_price('USDT', 'CAD')], index=[datetime.datetime.now()],
                               columns=['USDT (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "BCH":
            df1 = pd.DataFrame([get_crypto_price('BCH', 'CAD')], index=[datetime.datetime.now()],
                               columns=['Bitcoin Cash (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "LTC":
            df1 = pd.DataFrame([get_crypto_price('LTC', 'CAD')], index=[datetime.datetime.now()],
                               columns=['Litecoin (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "DOT":
            df1 = pd.DataFrame([get_crypto_price('DOT', 'CAD')], index=[datetime.datetime.now()],
                               columns=['Polkadot (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "DOGE":
            df1 = pd.DataFrame([get_crypto_price('DOGE', 'CAD')], index=[datetime.datetime.now()],
                               columns=['Dogecoin (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "ADA":
            df1 = pd.DataFrame([get_crypto_price('ADA', 'CAD')], index=[datetime.datetime.now()],
                               columns=['Cardona (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)

        if crypto == "SHIB":
            df1 = pd.DataFrame([get_crypto_price('SHIB', 'CAD')], index=[datetime.datetime.now()],
                               columns=['ShibaInu coin (CAD)'])

            my_chart = st.line_chart(df1)

            for i in range(100):
                animate(i,crypto)
                time.sleep(2)