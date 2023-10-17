import pandas as pd
import datetime

from analize import *

Posts:pd.DataFrame = pd.read_csv('./datasets/elonmusk.csv')
Tesla:pd.DataFrame = pd.read_csv('./datasets/tesla.csv')
Dogecoin:pd.DataFrame = pd.read_csv('./datasets/dogecoin.csv')

filter_list = []


influences = []#formatted: [i, date, text, trend]
for i, Post in Posts.iterrows():
    if not check_filter(str(Post["text"]), filter_list):
        continue
    else:
        #Convert Datetime-string, to Date-object
        date_time = datetime.datetime.strptime(str(Post["datetime"])[0:18], '%Y-%m-%d %H:%M:%S')
        date = date_time.date()

        trend = get_trend(date, Dogecoin)

        influences.append([i, date, Post["text"], trend])