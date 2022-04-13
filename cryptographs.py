
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt

import graph_color_decision

plt.style.use('ggplot')
def get_dot_graph():
    data = yf.download(tickers='DOT-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.dot_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_btc_graph():

    data = yf.download(tickers='BTC-CAD', period = '1wk', interval = '15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.bit_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt,use_container_width=True)
    plt.cla()

def get_eth_graph():
    data = yf.download(tickers='ETH-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.eth_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt,use_container_width=True)
    plt.cla()

def get_ltc_graph():
    data = yf.download(tickers='LTC-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.ltc_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_xlm_graph():
    data = yf.download(tickers='XLM-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.xlm_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_doge_graph():
    data = yf.download(tickers='DOGE-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.doge_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_bch_graph():
    data = yf.download(tickers='BCH-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.bch_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_ada_graph():
    data = yf.download(tickers='ADA-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.ada_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_shib_graph():
    data = yf.download(tickers='SHIB-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.shib_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()

def get_usdt_graph():
    data = yf.download(tickers='USDT-CAD', period='1wk', interval='15m')
    plt.figure().set_figheight(2)
    if graph_color_decision.usdt_color > 0.0:
        plt.plot(data.index,data['Close'],color="green",linewidth=3.0)
    else:
        plt.plot(data.index, data['Close'], color="red",linewidth=3.0)
    plt.axis('off')
    st.pyplot(plt)
    plt.cla()