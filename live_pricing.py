import streamlit as st
import cryptocompare
import datetime
import time
from datetime import datetime
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie_spinner

st.set_option('deprecation.showPyplotGlobalUse', False)
def live_price():


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets3.lottiefiles.com/private_files/lf30_h4qnjuax.json"
    lottie_json = load_lottieurl(lottie_url)

    '''with st_lottie_spinner(lottie_json):
        time.sleep(5)
        st.balloons()'''



    def get_crypto_price(cryptocurrency, currency):
        return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['BTC', 'ETH', 'XLM', 'USDT', 'BCH', 'LTC', 'DOT', 'DOGE', 'ADA', 'SHIB'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "BTC":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title="Bitcoin live price", xaxis_title="Time", yaxis_title= crypto +" Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                        values.append(get_crypto_price(crypto, 'CAD'))
                        times.append(datetime.now())
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)
                        time.sleep(3)

        if crypto == "ETH":
                plot_spot = st.empty()
                with st_lottie_spinner(lottie_json):
                    fig = go.FigureWidget()
                    fig.add_scatter(line=dict(color="#76D714"))
                    fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                    values = [get_crypto_price(crypto, 'CAD')]
                    times = []
                while True:
                    with plot_spot:
                        values.append(get_crypto_price(crypto, 'CAD'))
                        times.append(datetime.now())
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)
                        time.sleep(3)

        if crypto == "XLM":
                plot_spot = st.empty()
                with st_lottie_spinner(lottie_json):
                    fig = go.FigureWidget()
                    fig.add_scatter(line=dict(color="#76D714"))
                    fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                    values = [get_crypto_price(crypto, 'CAD')]
                    times = []
                while True:
                    with plot_spot:
                        values.append(get_crypto_price(crypto, 'CAD'))
                        times.append(datetime.now())
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)
                        time.sleep(3)

        if crypto == "USDT":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "BCH":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "LTC":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "DOT":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "DOGE":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "ADA":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                fig = go.FigureWidget()
                fig.add_scatter(line=dict(color="#76D714"))
                fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)

        if crypto == "SHIB":
            plot_spot = st.empty()
            with st_lottie_spinner(lottie_json):
                    fig = go.FigureWidget()
                    fig.add_scatter(line=dict(color="#76D714"))
                    fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
                    values = [get_crypto_price(crypto, 'CAD')]
                    times = []
            while True:
                with plot_spot:
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)
                    time.sleep(3)