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



        if submit_button:
                aus()

