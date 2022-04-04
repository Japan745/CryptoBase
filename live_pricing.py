import streamlit as st
import cryptocompare
import datetime
import time
from datetime import datetime
import plotly.graph_objects as go

st.set_option('deprecation.showPyplotGlobalUse', False)
def live_price():


    def get_crypto_price(cryptocurrency, currency):
        return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['BTC', 'ETH', 'XLM', 'USDT', 'BCH', 'LTC', 'DOT', 'DOGE', 'ADA', 'SHIB'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "BTC":
                plot_spot = st.empty()
                fig = go.FigureWidget()
                fig.add_scatter()
                fig.update_layout(title="Bitcoin live price", xaxis_title="Time", yaxis_title= crypto +" Price in CAD ")
                values = [get_crypto_price(crypto, 'CAD')]
                times = []
                while True:
                    with plot_spot:
                        time.sleep(3)
                        values.append(get_crypto_price(crypto, 'CAD'))
                        times.append(datetime.now())
                        fig.data[0].x = times
                        fig.data[0].y = values
                        st.plotly_chart(fig, use_container_width=True)

        if crypto == "ETH":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "XLM":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "USDT":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "BCH":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "LTC":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "DOT":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "DOGE":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "ADA":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)

        if crypto == "SHIB":
            plot_spot = st.empty()
            fig = go.FigureWidget()
            fig.add_scatter()
            fig.update_layout(title=crypto + " live price", xaxis_title="Time", yaxis_title=crypto + " Price in CAD ")
            values = [get_crypto_price(crypto, 'CAD')]
            times = []
            while True:
                with plot_spot:
                    time.sleep(3)
                    values.append(get_crypto_price(crypto, 'CAD'))
                    times.append(datetime.now())
                    fig.data[0].x = times
                    fig.data[0].y = values
                    st.plotly_chart(fig, use_container_width=True)