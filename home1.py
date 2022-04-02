import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

col1, col2, col3,= st.columns(3)


col1.metric("BTC","$45000" )
col1.text("This will go in FIRST column")

col2.metric("ETH", "25000")

col3.metric("DOT","52000" )

col4,col5,col6 =  st.columns(3)
col4.metric("BTC","$45000")
col5.metric("BTC","$45000" )
col6.metric("BTC","$45000" )
col7,col8,col9 =  st.columns(3)
col7.metric("BTC","$45000" )
col8.metric("BTC","$45000" )
col9.metric("BTC","$45000" )
#col10.metric("BTC","$45000" )


