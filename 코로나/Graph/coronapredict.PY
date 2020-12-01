import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot
import numpy as np

data = pd.read_csv('data.csv', error_bad_lines=False)
print(data.head())
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data['date'],
        y=data['Additional'],
        name='Confirmed in Korea'
    )
)

df_prophet = data.rename(columns={
    'date': 'ds',
    'Additional': 'y'
})
m = Prophet(
    changepoint_prior_scale=0.2,
    changepoint_range=0.98,
    yearly_seasonality=False,
    weekly_seasonality=True,
    daily_seasonality=True,
    seasonality_mode='multiplicative'

)
m.add_seasonality('quarterly', period=14,fourier_order=10, mode='multiplicative')

m.fit(df_prophet) #학습시작

future = m.make_future_dataframe(periods=7) #예측할 공간 할당
forecast = m.predict(future) #forecast에 예측값 할당
fig = plot_plotly(m, forecast)
py.plot(fig)
# fig.show()
# fig = m.plot(forecast)
# a = add_changepoints_to_plot(fig.gca(), m, forecast)
# fig.show()



# fig = m.plot(forecast)
# a = add_changepoints_to_plot(fig.gca(), m, forecast)
# a = add_changepoints_to_plot(fig.gca(), m, forecast)
# py.plot(fig)


