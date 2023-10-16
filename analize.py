#from datetime import datetime
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

def get_trade_day_avg(date, stock):
    trade_day = stock.loc[stock['date'] == str(date.strftime('%Y-%m-%d'))]

    if trade_day.empty:
        return None
    
    else:

        trade_day_open = trade_day.open.item()
        trade_day_close = trade_day.close.item()
        trade_day_avg = (trade_day_open + trade_day_close) / 2

        return trade_day_avg


def get_dates(date, interval_length:int=5):
    dates = []

    for i in range(0, interval_length):
        date += datetime.timedelta(days=interval_length)
        dates.append(date)

    return dates


def get_trend(date, stock, interval_length:int=5):
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

    model = LinearRegression()
    model.fit(x, y)

    return model.coef_