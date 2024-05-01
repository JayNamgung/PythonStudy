import pandas_datareader as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2019, 12, 31)
    
'''
원하는 값 불러오기 가능
DCOILWITCO : 원자재
'''

oil = web.DataReader('DCOILWITCO', 'fred', start, end)
oil.head()