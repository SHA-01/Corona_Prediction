import csv
import matplotlib.dates as mdates
import numpy as np
import matplotlib.pyplot as plt
import copy
f = open('data.csv', 'r', encoding='utf-8')
rd = csv.reader(f)
daylist = []
confirmerlist = []
for i in list(rd)[1:]:
    daylist.append(i[0])
    confirmerlist.append(int(i[2])) #저장된 csv파일을 읽어와서 날짜와 추가 확진자수를 가져온다.
logdata = []
print(confirmerlist)
for i in confirmerlist:
    try:
        temp1 = np.log10(int(i))
        logdata.append(temp1)
    except ValueError:
        temp1 = -0.01
        logdata.append(temp1)  # 확진자수의 변동이 크므로 로그값을 취한다

derivative = np.diff(np.diff(confirmerlist))
next_v = 0
cur_v = 0
crucial_day = []
# plt.figure(figsize=(500, 30))

plt.plot(daylist, confirmerlist) # 확진자수의 그래프를 구함
newdaylist = copy.deepcopy(daylist)
newdaylist.remove(daylist[0])
newdaylist.remove(daylist[-1])
plt.plot(newdaylist, derivative)
#이계도함수 구함
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.show()

plt.xticks(range(len(confirmerlist)))  # add loads of ticks
plt.grid()
for i in range(len(derivative)-1):
    cur_v = derivative[i]
    next_v = derivative[i+1]
    if cur_v >= 0 and next_v < 0 and abs(cur_v-next_v) > 150:
        # print(daylist[i+1], ": ",cur_v, next_v)
        crucial_day.append(daylist[i+1])
        plt.axvspan(daylist[i], daylist[i+1], facecolor='red')
    if cur_v <= 0 and next_v > 0 and abs(cur_v-next_v) > 150:
        # print(daylist[i+1], ": ", cur_v, next_v)
        crucial_day.append(daylist[i+1])
        plt.axvspan(daylist[i], daylist[i+1], facecolor='red')
#그래프의 변곡점을 구해서 색칠함
# plt.plot(x[1:], y[1:], 'ro')
# plt.plot(x[0], y[0], 'g*')

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2  # inch margin
s = maxsize/plt.gcf().dpi*len(confirmerlist)+2*m
margin = m/plt.gcf().get_size_inches()[0]
plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
# 그래프의 크기 설정

plt.tick_params(axis='x', labelrotation=60)
#x축의 글씨 회전
plt.savefig(__file__+".png")
# print(crucial_day)
# print(derivative)
# print(confirmerlist)
plt.show()
