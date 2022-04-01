import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.tools

def home():


        st.title('Cryptocurrency prediction.')
        def aus():
                import pandas as pd
                import numpy as np
                import pandas_datareader as web
                import datetime as dt


                start = dt.datetime(2020, 1, 1)
                end = dt.datetime.now()

                df = web.DataReader('XRP-USD', 'yahoo', start, end)
                #df




                fig = (df['Adj Close'].plot())
                st.plotly_chart(fig.figure, use_container_width=True)

        with st.form(key='my_form'):
                crypto = st.selectbox('Select Cryptocurrency', ['BTC', 'ETH', 'XLM','USDT', 'BCH','LTC','DOT','DOG','ADA','SHI'])
                start = st.date_input('Start')
                end = st.date_input('End')
                submit_button = st.form_submit_button(label='Submit')

        if submit_button:
                aus()

