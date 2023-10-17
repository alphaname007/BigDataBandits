import time
import pandas as pd
import datetime

from analize import *

runtime_start = time.time()

Posts:pd.DataFrame = pd.read_csv('./datasets/elonmusk.csv')
Tesla:pd.DataFrame = pd.read_csv('./datasets/tesla.csv')
Dogecoin:pd.DataFrame = pd.read_csv('./datasets/dogecoin.csv')

filter_list = []#"dogecoin", "Doge"]

def get_runtime(runtime_start:time=runtime_start):
    return round(time.time() - runtime_start, 4)


influences:pd.DataFrame = pd.DataFrame(columns=['date', 'text', 'trend'])

for i, Post in Posts.iterrows():
    if not check_filter(str(Post['text']), filter_list, hit=False):
        print(f'{get_runtime()} PASS')
        continue
    else:
        #Convert Datetime-string, to Date-object
        date_time = datetime.datetime.strptime(str(Post['datetime'])[0:18], '%Y-%m-%d %H:%M:%S')
        date = date_time.date()

        trend = get_trend(date, Dogecoin)
        if trend == None:
            print(f'{get_runtime()} NONE')
            continue

        
        influences.loc[i] = [date] + [Post['text']] + [trend]
        print(f'{get_runtime()} HIT')

max_influence = influences.loc[influences['trend'] == influences["trend"].max()]
avg_influence_trend = influences.loc[:, 'trend'].mean()

print(max_influence)
print(avg_influence_trend)

runtime_elapsed = get_runtime()

print(f'RUNTIME: {runtime_elapsed}')