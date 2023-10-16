import pandas as pd
import datetime

from analize import *

Posts = pd.read_csv('elonmusk.csv')
Tesla = pd.read_csv('tesla.csv')
Dogecoin = pd.read_csv('dogecoin.csv')

for i, Post in Posts.iterrows():
    #Convert Datetime-string, to Datetime-object
    date_time = datetime.datetime.strptime(str(Post["datetime"])[0:18], '%Y-%m-%d %H:%M:%S')
    date_time = date_time.strptime("2023-06-27 23:12:47", '%Y-%m-%d %H:%M:%S')
    date = date_time.date()

    print(get_trend(date, Tesla))

    #text = Post['text']

    #print(f'Elon Musk {date_time} ')