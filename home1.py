import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")

with open('homeview') as f:
   st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



col1, col2, col3,= st.columns(3)

with col1:
   st.header("BTC")
   st.image("images/bitcoin.png", width=40)
   st.markdown("**$42000**")
with col2:
   st.header("ETH")
   st.image("images/ethereum.png",width=40)
   st.markdown("**$42000**")
with col3:
   st.header("LTC")
   st.image("images/litecoin.png",width=40)
   st.markdown("**$42000**")


col4,col5,col6 =  st.columns(3)
with col4:
   st.header("DOGE")
   st.image("images/dogecoin.png", width=40)
   st.markdown("**$42000**")
with col5:
   st.header("ADA")
   st.image("images/adacoin.png",width=40)
   st.markdown("**$42000**")
with col6:
   st.header("SHIB")
   st.image("images/shibacoin.png",width=40)
   st.markdown("**$42000**")


col7,col8,col9, =  st.columns(3)
with col7:
   st.header("XLM")
   st.image("images/xlmcoin.png", width=40)
   st.markdown("**$42000**")
with col8:
   st.header("USDT")
   st.image("images/usdtcoin.png",width=40)
   st.markdown("**$42000**")
with col9:
   st.header("BCH")
   st.image("images/bshcoin.png",width=40)
   st.markdown("**$42000**")




col10,col11,col12,=st.columns(3)
with col10:
   st.header("DOT")
   st.image("images/polkadotcoin.png",width=40)
   st.markdown("**$42000**")
with col11:
   st.empty()

with col12:
   st.empty()
