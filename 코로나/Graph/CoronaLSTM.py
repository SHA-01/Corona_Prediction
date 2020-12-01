import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
import csv


daylist = []
mylist = []
confirmerlist = []


dataset = pd.read_csv('data.csv')
print(dataset.head())
data = dataset.dropna()

seq_len = 50
sequence_length = seq_len + 1

Confirmers = data['Additional'].values
result = []
for index in range(len(Confirmers) - sequence_length):
    result.append(Confirmers[index: index + sequence_length])
#데이터를 50개씩 자름
normalized_data = []
for window in result:
    try:
        normalized_window = [((float(p) / float(window[0])) - 1)
                             for p in window]
        normalized_data.append(normalized_window)
    except ZeroDivisionError:
        normalized_window = [
            (float(p) / (float(window[0]+0.01)) - 1) for p in window]
        normalized_data.append(normalized_window)
#데이터를 정규화함
result = np.array(normalized_data)
# print(normalized_data)
row = int(round(result.shape[0] * 0.9))
train = result[:row, :] #트레이닝셋을 90%할당
np.random.shuffle(train) # 트레이닝셋을 랜덤으로 섞음

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]
print(x_test, y_test)

model = Sequential()

model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))

model.add(LSTM(64, return_sequences=False))

model.add(Dense(1, activation='linear'))

model.compile(loss='mse', optimizer='rmsprop') #mse =Mean Squared Error

model.summary()

model.fit(x_train, y_train,
          validation_data=(x_test, y_test),
          batch_size=10,
          epochs=20)
pred = model.predict(x_test)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
# plt.plot(daylist, confirmerlist)
ax.plot(pred, label='Prediction')
ax.legend()
plt.show()
# https://www.youtube.com/watch?v=sG_WeGbZ9A4p
