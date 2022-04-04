import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.tools
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def get_home():
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': 'f196187f-d576-4c6c-8d4c-d35a4bab8511',
        }
        def get_btc():
                parameters = {'slug': 'bitcoin', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['1']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['1']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['1']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['1']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['1']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['1']['quote']['CAD']['volume_change_24h']
                col1, col2, col3, = st.columns(3)

                with col1:
                        st.metric(label="Bitcoin (BTC)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col2:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col3:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)), delta=str(round(marketcap_ch, 2)) + "%")

        def get_eth():
                parameters = {'slug': 'ethereum', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['1027']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['1027']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['1027']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['1027']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['1027']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['1027']['quote']['CAD']['volume_change_24h']
                col4, col5, col6, = st.columns(3)

                with col4:
                        st.metric(label="Ethereum (ETH)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col5:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col6:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        def get_xlm():
                parameters = {'slug': 'stellar', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['512']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['512']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['512']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['512']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['512']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['512']['quote']['CAD']['volume_change_24h']
                col7, col8, col9, = st.columns(3)

                with col7:
                        st.metric(label="Stellar (XLM)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col8:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col9:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        def get_usdt():
                parameters = {'slug': 'tether', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['825']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['825']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['825']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['825']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['825']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['825']['quote']['CAD']['volume_change_24h']
                col10, col11, col12, = st.columns(3)

                with col10:
                        st.metric(label="Tether (USDT)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col11:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col12:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        def get_bch():
                parameters = {'slug': 'bitcoin-cash', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['1831']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['1831']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['1831']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['1831']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['1831']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['1831']['quote']['CAD']['volume_change_24h']
                col13, col14, col15, = st.columns(3)

                with col13:
                        st.metric(label="Bitcoin cash (BCH)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col14:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col15:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        def get_ltc():
                parameters = {'slug': 'litecoin', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['2']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['2']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['2']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['2']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['2']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['2']['quote']['CAD']['volume_change_24h']
                col16, col17, col18, = st.columns(3)

                with col16:
                        st.metric(label="Litecoin (LTC)", value=str(round(price, 2)),delta=str(round(hour24, 2)) + "%")
                with col17:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col18:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        def get_dot():
                parameters = {'slug': 'polkadot', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['6636']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['6636']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['6636']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['6636']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['6636']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['6636']['quote']['CAD']['volume_change_24h']
                col19, col20, col21, = st.columns(3)

                with col19:
                        st.metric(label="Polkadot (DOT)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col20:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col21:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        def get_doge():
                parameters = {'slug': 'dogecoin', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['74']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['74']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['74']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['74']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['74']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['74']['quote']['CAD']['volume_change_24h']
                col22, col23, col24, = st.columns(3)

                with col22:
                        st.metric(label="Dogecoin (DOGE)", value=str(round(price, 2)), delta=str(round(hour24, 2)) + "%")
                with col23:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col24:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")


        def get_ada():
                parameters = {'slug': 'cardano', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['2010']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['2010']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['2010']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['2010']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['2010']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['2010']['quote']['CAD']['volume_change_24h']
                col25, col26, col27, = st.columns(3)

                with col25:
                        st.metric(label="Cardano (ADA)", value=str(round(price, 2)),delta=str(round(hour24, 2)) + "%")
                with col26:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col27:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")


        def get_shib():
                parameters = {'slug': 'shiba-inu', 'convert': 'CAD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['5994']['quote']['CAD']['percent_change_24h']
                price = json.loads(response.text)['data']['5994']['quote']['CAD']['price']
                marketcap = json.loads(response.text)['data']['5994']['quote']['CAD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['5994']['quote']['CAD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['5994']['quote']['CAD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['5994']['quote']['CAD']['volume_change_24h']
                col28, col29, col30, = st.columns(3)

                with col28:
                        st.metric(label="Shiba Inu (SHIB)", value=str(round(price,2)), delta=str(round(hour24, 2)) + "%")
                with col29:
                        st.metric(label="Volume", value=str(round(volume, 2)), delta=str(round(volume_ch, 2)) + "%")
                with col30:
                        st.metric(label="Market Cap", value=str(round(marketcap, 2)),delta=str(round(marketcap_ch, 2)) + "%")

        #col1, col2, col3, = st.columns(3)

        #with col1:
        get_btc()
        #with col2:
        get_eth()
       # with col3:
        get_xlm()

       # col4, col5, col6 = st.columns(3)

       # with col4:
        get_usdt()
       # with col5:
        get_bch()
        #with col6:
        get_ltc()

        #col7, col8, col9 = st.columns(3)

        #with col7:
        get_dot()
        #with col8:
        get_doge()
        #with col9:
        get_ada()

        #col10,col11 = st.columns(2)

        #with col10:
        get_shib()

