import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot
import numpy as np
import matplotlib.pyplot as plt
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
    weekly_seasonality=False,
    daily_seasonality=False,
    seasonality_mode='multiplicative'  # 코로나 확진자수는 곱해가면서 증가하는 모델을 사용해 예측함
) 
m.add_seasonality('quarterly', period=365.25/4,fourier_order=5, prior_scale=15) 
m.add_seasonality('daily', period=1,fourier_order=50) 
m.add_seasonality('weekly', period=7, fourier_order=20)
m.add_seasonality('monthly', period=30.5,fourier_order=55)
m.fit(df_prophet) #학습시작

future = m.make_future_dataframe(periods=7) #예측할 공간 할당
forecast = m.predict(future) #forecast에 예측값 할당
fig = plot_plotly(m, forecast)
py.plot(fig)

fig= m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)
plt.savefig(__file__+".png")
plt.show()
# fig.show()
# fig = m.plot(forecast)
# a = add_changepoints_to_plot(fig.gca(), m, forecast)
# fig.show()



# fig = m.plot(forecast)
# a = add_changepoints_to_plot(fig.gca(), m, forecast)
# a = add_changepoints_to_plot(fig.gca(), m, forecast)
# py.plot(fig)


