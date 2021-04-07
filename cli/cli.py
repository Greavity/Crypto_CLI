import argparse
from coinpaprika import client as coinpaprika
from datetime import date, timedelta
from functools import reduce
from calendar import monthrange
import time


def average_price(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


def days_in_month(year, month):
    num_days = monthrange(year, month)[1]
    days = [date(year, month, day) for day in range(1, num_days + 1)]
    return days


def date_formatting(old_date):
    return date(int(old_date[2]), int(old_date[1]), int(old_date[0]))


client = coinpaprika.Client()

prices = []

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--average', help=' date format DD-MM-YYYY')
parser.add_argument('--start_date', help='start date')
parser.add_argument('--end_date', help='end date')
args = parser.parse_args()

s = '01-' + args.start_date
e = '01-' + args.end_date

start = s.split('-')
end = e.split('-')

sdate = date_formatting(start)
edate = date_formatting(end)

delta = edate - sdate
for i in range(delta.days + 1):
    time.sleep(0.1)
    day = str(sdate + timedelta(days=i))
    ohlc = client.candles('btc-bitcoin', start=day)
    for d in ohlc:
        close = d['close']
        prices.append(close)
aver = average_price(prices)
print(aver)
