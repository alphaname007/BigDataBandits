import time
import pandas as pd
import datetime

from analize import *

runtime_start = time.time()

Posts:pd.DataFrame = pd.read_csv('./datasets/elonmusk.csv')
Tesla:pd.DataFrame = pd.read_csv('./datasets/tesla.csv')
Dogecoin:pd.DataFrame = pd.read_csv('./datasets/dogecoin.csv')

filter_list = []


influences:pd.DataFrame = pd.DataFrame(columns=['i', 'date', 'text', "trend"])

for i, Post in Posts.iterrows():
    if not check_filter(str(Post["text"]), filter_list, hit=False):
        print(f"{time.time()-runtime_start} PASS")
        continue
    else:
        #Convert Datetime-string, to Date-object
        date_time = datetime.datetime.strptime(str(Post["datetime"])[0:18], '%Y-%m-%d %H:%M:%S')
        date = date_time.date()

        trend = get_trend(date, Dogecoin)
        if trend == None:
            print(f"{time.time()-runtime_start} NONE")
            continue

        
        influences.loc[i] = [i] + [date] + [Post['text']] + [trend]
        print(f"{time.time()-runtime_start} HIT")

print(influences)

runtime_end = time.time()
runtime_elapsed = runtime_end - runtime_start

print(f"RUNTIME: {runtime_elapsed}")