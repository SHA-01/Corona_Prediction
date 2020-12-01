import pandas as pd
import plotly.graph_objs as go
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot
import numpy as np
import matplotlib.pyplot as plt
# Confirmation, recovery, and death data sets by region worldwide
# 전세계 지역별 확진자, 회복자, 사망자 Data Set
reqData = 'Additional'
data = pd.read_csv('data.csv', error_bad_lines=False)
print(data.head())
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=data.date,
#         y=data[reqData],
#         name='Confirmed in Korea'
#     )
# )

df_prophet = data.rename(columns={
    'date': 'ds',
    reqData: 'y'
})
m = Prophet(
    changepoint_prior_scale=0.2,
    changepoint_range=0.98,
    yearly_seasonality=False,
    weekly_seasonality=True,
    daily_seasonality=True,
    seasonality_mode='multiplicative'

)
m.add_seasonality('quarterly', period=14,
                  fourier_order=10, mode='multiplicative')
m.fit(df_prophet)

future = m.make_future_dataframe(periods=7)
forecast = m.predict(future)
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)
plt.savefig(__file__+".png")
plt.show()

