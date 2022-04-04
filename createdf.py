import datetime
import time

import streamlit as st
import pandas as pd
import cryptocompare


def get_crypto_price(cryptocurrency, currency):
    return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

df1 = pd.DataFrame([get_crypto_price('ETH', 'CAD')], index=[datetime.datetime.now()],columns=['Bitcoin (CAD)'])

def animate(i):
    df2 = pd.DataFrame([get_crypto_price('ETH', 'CAD')], index=[datetime.datetime.now()],columns=['Bitcoin (CAD)'])

    my_chart.add_rows(df2)


my_chart = st.line_chart(df1)

for i in range(100) :

    animate(i)
    time.sleep(20)




