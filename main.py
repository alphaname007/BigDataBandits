import time
import pandas as pd
import datetime

from analize import *
from visulize import *

runtime_start = time.time()

Posts:pd.DataFrame = pd.read_csv('./datasets/elonmusk.csv')
Tesla:pd.DataFrame = pd.read_csv('./datasets/tesla.csv')
Dogecoin:pd.DataFrame = pd.read_csv('./datasets/dogecoin.csv')

filter_list = []#"dogecoin", "Doge"]

def get_runtime(runtime_start:time=runtime_start):
    return round(time.time() - runtime_start, 4)

def append_item(list:list, item):
    list.append(item)

influences:pd.DataFrame = pd.DataFrame(columns=['date', 'posts', 'count_posts', 'trend'])
j = 0
old_date = None

for i, Post in Posts.iterrows():
    if not check_filter(str(Post['text']), filter_list, hit=False):
        print(f'{get_runtime()} PASS')
        continue
    else:
        #Convert Datetime-string, to Date-object
        date = datetime.datetime.strptime(str(Post['datetime'])[0:18], '%Y-%m-%d %H:%M:%S').date()

        ret = get_trend(date, Dogecoin)
        if ret == None:
            print(f'{get_runtime()} NONE')
            continue
        
        else:
            print(f'{get_runtime()} HIT')
            trend, avgs, dates, model = ret

            if date != old_date:
                influences.loc[j] = [date] + [[Post['text']]] + [0] + [trend]
                old_date = date
                old_j = j
                j += 1
            else:
                influences.loc[j-1, 'posts'].append(Post['text'])
                influences.loc[j-1, 'count_posts'] += 1

visulize_trends(influences['trend'])


max_influence = influences.loc[influences['trend'] == influences["trend"].max()]
avg_influence_trend = influences.loc[:, 'trend'].mean()

print(max_influence)
print(avg_influence_trend)

runtime_elapsed = get_runtime()

print(f'RUNTIME: {runtime_elapsed}')