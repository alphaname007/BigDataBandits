import math
import datetime
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def check_filter(text:str, filter_list:list, hit:bool):
    for filter in filter_list:
        if filter in text:
            return hit
    return not hit


def get_trade_day_avg(date:datetime, stock:pd.DataFrame):
    trade_day = stock.loc[stock['date'] == str(date.strftime('%Y-%m-%d'))]

    if trade_day.empty:
        return None
    
    else:

        trade_day_open = trade_day.open.item()
        trade_day_close = trade_day.close.item()
        trade_day_avg = (trade_day_open + trade_day_close) / 2

        return trade_day_avg


def get_dates(date:datetime, interval_length:int=5):
    dates = []

    for i in range(0, interval_length):
        date += datetime.timedelta(days=i)
        dates.append(date)

    return dates


def get_trend(date:datetime, stock:pd.DataFrame, interval_length:int=5):
    dates:list = get_dates(date, interval_length) 
    avgs:list = []

    for date_i in dates:
        avg = get_trade_day_avg(date_i, stock)
        if avg == None:
            return None
        else:
            avgs.append(avg)
    
    x = np.array(list(range(0, interval_length))).reshape((-1, 1))
    y = np.array(avgs)

    model = LinearRegression().fit(x, y)

    start_price_model = model.predict([[0]])[0]
    end_price_model = model.predict([[interval_length]])[0]

    change_percentage = round((end_price_model / start_price_model), 4)

    return [change_percentage, avgs, dates, (start_price_model, end_price_model)]