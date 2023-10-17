import pandas as pd
import datetime

from analize import *

Posts:pd.DataFrame = pd.read_csv('./datasets/elonmusk.csv')
Tesla:pd.DataFrame = pd.read_csv('./datasets/tesla.csv')
Dogecoin:pd.DataFrame = pd.read_csv('./datasets/dogecoin.csv')

for i, Post in Posts.iterrows():
    #Convert Datetime-string, to Date-object
    date_time = datetime.datetime.strptime(str(Post["datetime"])[0:18], '%Y-%m-%d %H:%M:%S')
    date = date_time.date()

    print(get_trend(date, Dogecoin))