import streamlit as st
import cryptocompare
import datetime
import time
from datetime import datetime
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie_spinner
from pytz import timezone

st.set_option('deprecation.showPyplotGlobalUse', False)
def live_price():

    timezoneca = "Canada/Eastern"
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets3.lottiefiles.com/private_files/lf30_h4qnjuax.json"
    lottie_json = load_lottieurl(lottie_url)

    def get_crypto_price(cryptocurrency, currency):
        return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Stellar (XLM)', 'Tether (USDT)', 'Bitcoin Cash (BCH)',
                               'Litecoin (LTC)', 'Polkadot (DOT)', 'Dogecoin (DOGE)', 'Cardano (ADA)', 'Shiba Inu (SHIB)'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "Bitcoin (BTC)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="Bitcoin live price", xaxis_title="Time", yaxis_title= crypto +" Price in CAD ")
                values = [get_crypto_price('BTC', 'CAD')]
                times = []
            while True:
                with plot_spot:
                        values.append(get_crypto_price('BTC', 'CAD'))
                        times.append(datetime.now(timezone(timezoneca)))
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)
                        time.sleep(3)

        if crypto == "Ethereum (ETH)":
                plot_spot = st.empty()
                with st_lottie_spinner(lottie_json):
                    fig = go.FigureWidget()
                    fig.add_scatter(line=dict(color="#76D714"))
                    fig.update_layout(title="ETH" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                    values = [get_crypto_price('ETH', 'CAD')]
                    times = []
                while True:
                    with plot_spot:
                        values.append(get_crypto_price('ETH', 'CAD'))
                        times.append(datetime.now(timezone(timezoneca)))
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)
                        time.sleep(3)

        if crypto == "Stellar (XLM)":
                plot_spot = st.empty()
                with st_lottie_spinner(lottie_json):
                    fig = go.FigureWidget()
                    fig.add_scatter(line=dict(color="#76D714"))
                    fig.update_layout(title="XLM" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                    values = [get_crypto_price('XLM', 'CAD')]
                    times = []
                while True:
                    with plot_spot:
                        values.append(get_crypto_price('XLM', 'CAD'))
                        times.append(datetime.now(timezone(timezoneca)))
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)
                        time.sleep(3)

        if crypto == "Tether (USDT)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="USDT" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price('USDT', 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price('USDT', 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "Bitcoin Cash (BCH)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="BCH" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price('BCH', 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price('BCH', 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "Litecoin (LTC)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="LTC" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price('LTC', 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price('LTC', 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "Polkadot (DOT)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="DOT" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price('DOT', 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price('DOT', 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "Dogecoin (DOGE)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="DOGE" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price('DOGE', 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price('DOGE', 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "Cardano (ADA)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="ADA" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price('ADA', 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price('ADA', 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "Shiba Inu (SHIB)":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                    fig = go.FigureWidget()
                    fig.add_scatter(line=dict(color="#76D714"))
                    fig.update_layout(title="SHIB" + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                    values = [get_crypto_price("SHIB", 'CAD')]
                    times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price("SHIB", 'CAD'))
                    times.append(datetime.now(timezone(timezoneca)))
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)