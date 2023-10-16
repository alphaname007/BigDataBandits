import pandas as pd
from datetime import datetime

Tweets = pd.read_csv('elonmusk.csv')
Tesla = pd.read_csv('tesla.csv')
Dogecoin = pd.read_csv('dogecoin.csv')

for i, Tweet in Tweets.iterrows():
    date = datetime.strptime(str(Tweet["datetime"])[0:10], '%Y-%m-%d')
    text = Tweet['text']
    print(f'Elon Musk {date} ')