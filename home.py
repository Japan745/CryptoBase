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


import cryptographs
import graph_color_decision



def get_home():
        with open('homeview') as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
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
                week_per_ch = json.loads(response.text)['data']['1']['quote']['CAD']['percent_change_7d']
                graph_color_decision.bit_color = week_per_ch
                cl1,col1, col2, col3,col4,g1 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl1:
                        st.write(1)
                with col1:
                        st.image("Images/bitcoin-2.png")
                with col2:
                        st.metric(label='Bitcoin BTC ', value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col3:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col4:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))), delta=str(round(marketcap_ch, 2)) + "%")
                with g1:
                        st.write("7 days graph")
                        cryptographs.get_btc_graph()

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
                week_per_ch = json.loads(response.text)['data']['1027']['quote']['CAD']['percent_change_7d']
                graph_color_decision.eth_color = week_per_ch
                cl2,col5, col6, col7,col8,g2 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl2:
                        #cryptographs.get_eth_graph()
                        st.write(2)
                with col5:
                        st.image("Images/img/ethereum.png")
                with col6:
                        st.metric(label="Ethereum (ETH)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col7:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col8:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g2:
                        st.write("7 days graph")
                        cryptographs.get_eth_graph()

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
                week_per_ch = json.loads(response.text)['data']['512']['quote']['CAD']['percent_change_7d']
                graph_color_decision.xlm_color = week_per_ch
                cl3,col9, col10, col11,col12,g3 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl3:
                        st.write(3)
                with col9:
                        st.image("Images/img/xlmcoin.png")
                with col10:
                        st.metric(label="Stellar (XLM)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col11:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col12:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g3:
                        st.write("7 days graph")
                        cryptographs.get_xlm_graph()

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
                week_per_ch = json.loads(response.text)['data']['825']['quote']['CAD']['percent_change_7d']
                graph_color_decision.usdt_color = week_per_ch
                cl4,col13, col14, col15,col16,g4 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl4:
                        st.write(4)
                with col13:
                        st.image("Images/img/usdtcoin.png")
                with col14:
                        st.metric(label="Tether (USDT)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col15:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col16:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g4:
                        st.write("7 days graph")
                        cryptographs.get_usdt_graph()

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
                week_per_ch = json.loads(response.text)['data']['1831']['quote']['CAD']['percent_change_7d']
                graph_color_decision.bch_color = week_per_ch
                cl5,col17, col18, col19,col20,g5 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl5:
                        st.write(5)
                with col17:
                        st.image("Images/img/bshcoin.png")
                with col18:
                        st.metric(label="Bitcoin cash (BCH)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col19:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col20:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g5:
                        st.write("7 days graph")
                        cryptographs.get_bch_graph()

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
                week_per_ch = json.loads(response.text)['data']['2']['quote']['CAD']['percent_change_7d']
                graph_color_decision.ltc_color = week_per_ch
                cl6,col21, col22, col23,col24,g6 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl6:
                        st.write(6)
                with col21:
                        st.image("Images/img/litecoin.png")
                with col22:
                        st.metric(label="Litecoin (LTC)", value=("$"+str(round(price, 2))),delta=str(round(hour24, 2)) + "%")
                with col23:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col24:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g6:
                        st.write("7 days graph")
                        cryptographs.get_ltc_graph()

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
                week_per_ch = json.loads(response.text)['data']['6636']['quote']['CAD']['percent_change_7d']
                graph_color_decision.dot_color = week_per_ch
                cl7,col25, col26, col27,col28,g7 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl7:
                        st.write(7)
                with col25:
                        st.image("Images/img/polkadotcoin.png")
                with col26:
                        st.metric(label="Polkadot (DOT)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col27:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col28:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g7:
                        st.write("7 days graph")
                        cryptographs.get_dot_graph()

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
                week_per_ch = json.loads(response.text)['data']['74']['quote']['CAD']['percent_change_7d']
                graph_color_decision.doge_color = week_per_ch
                cl8,col29, col30, col31,col32,g8 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl8:
                        st.write(8)
                with col29:
                        st.image("Images/img/dogecoin.png")
                with col30:
                        st.metric(label="Dogecoin (DOGE)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col31:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col32:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g8:
                        st.write("7 days graph")
                        cryptographs.get_doge_graph()


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
                week_per_ch = json.loads(response.text)['data']['2010']['quote']['CAD']['percent_change_7d']
                graph_color_decision.ada_color = week_per_ch
                cl9,col33, col34, col35,col36,g9 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl9:
                        st.write(9)
                with col33:
                        st.image("Images/img/adacoin.png")
                with col34:
                        st.metric(label="Cardano (ADA)", value=("$"+str(round(price, 2))),delta=str(round(hour24, 2)) + "%")
                with col35:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col36:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g9:
                        st.write("7 days graph")
                        cryptographs.get_ada_graph()


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
                week_per_ch = json.loads(response.text)['data']['5994']['quote']['CAD']['percent_change_7d']
                graph_color_decision.shib_color = week_per_ch
                cl10,col37, col38, col39,col40,g10 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl10:
                        st.write(10)
                with col37:
                        #st.metric(label="Shiba Inu (SHIB)", value=str(st.image("Images/img/shibacoin.png")), delta="SHIB-CAD")
                        #st.subheader("Shiba Inu (SHIB)")
                        st.image("Images/img/shibacoin.png")
                with col38:
                        st.metric(label="Shiba Inu (SHIB)", value=("$"+str(round(price,5))), delta=str(round(hour24, 2)) + "%")
                with col39:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col40:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g10:
                        st.write("7 days graph")
                        cryptographs.get_shib_graph()

        #col1, col2, col3, = st.columns(3)

        #with col1:
        st.write(" ")
        hide_img_fs = '''
                <style>
                button[title="View fullscreen"]{
                    visibility: hidden;}
                </style>
                '''

        st.markdown(hide_img_fs, unsafe_allow_html=True)
        get_btc()
        st.write("---------------------------")
        #with col2:
        get_eth()
        st.write("---------------------------")
       # with col3:
        get_xlm()
        st.write("---------------------------")
       # col4, col5, col6 = st.columns(3)

       # with col4:
        get_usdt()
        st.write("---------------------------")
       # with col5:
        get_bch()
        st.write("---------------------------")
        #with col6:
        get_ltc()
        st.write("---------------------------")

        #col7, col8, col9 = st.columns(3)

        #with col7:
        get_dot()
        st.write("---------------------------")
        #with col8:
        get_doge()
        st.write("---------------------------")
        #with col9:
        get_ada()
        st.write("---------------------------")
        #col10,col11 = st.columns(2)

        #with col10:
        get_shib()



