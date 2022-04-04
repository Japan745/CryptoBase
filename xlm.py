import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import statsmodels.api as sm



def get_xlm():
            XLM = yf.download("XLM-CAD")
            XLM = XLM.drop(columns=['Open','High','Low','Close','Volume'])
            modelhigh = sm.tsa.statespace.SARIMAX(XLM['Adj Close'],
                                                  order=(1, 0, 0),
                                                  seasonal_order=(1, 0, 1, 12),
                                                  enforce_stationarity=False,
                                                  enforce_invertibility=False)
            resultshigh = modelhigh.fit()
            pred = resultshigh.get_prediction(start=datetime(2019, 1, 1), dynamic=False)
            pred_ci = pred.conf_int()
            ax = XLM['2017':].plot(label='observed')
            pred.predicted_mean.plot(ax=ax, label='Forecasted', alpha=.2, figsize=(14, 7))
            pred_uc = resultshigh.get_forecast(steps=180)
            pred_ci = pred_uc.conf_int()
            ax = XLM.plot(label='observed', color='Grey', figsize=(20, 8))
            One_week_values = pred_uc.predicted_mean[:7]
            One_week_values = round(One_week_values, 2)
            pred_uc.predicted_mean.plot(ax=ax, color='green', label='Forecast')
            ax.set_xlabel('Date')
            ax.set_ylabel('CAD price')
            plt.legend()
            #space = st.pyplot
            with st.expander("Wanna see (All time graph + predicted graph)"):
                st.pyplot(plt, use_container_width=True)
            #printing 6 months values
            st.header("6 Months Forecasting")
            fig = px.line(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean.values,
                          labels={'x': 'Date', 'y': 'Canadian Dollars'}, title="Stellar (XLM) forecasting",
                          markers=True)
            with st.expander("View",True):
                st.plotly_chart(fig, use_container_width=True)
            #printing one week values
            st.header("One Week Forecasting")
            fig = px.line(x=One_week_values.index, y=One_week_values.values,
                          labels={'x': 'Date', 'y': 'Canadian Dollars'}, title="Stellar (XLM) forecasting",
                          markers=True)
            with st.expander("View", True):
                st.plotly_chart(fig, use_container_width=True)