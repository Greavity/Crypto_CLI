from coinpaprika import client as coinpaprika
import json
from functools import reduce
from datetime import date, timedelta
from functools import reduce
from calendar import monthrange


# client = coinpaprika.Client()
# coin = 'btc-bitcoin'
# ohlc = client.candles(coin, start='2019-10-15')
#
# for d in ohlc:
#     close = d['close']
#
#
# def average_price(lst):
#     return reduce(lambda a, b: a + b, lst) / len(lst)


# def save_request():
#     with open('write_file.json', 'w') as write_file:
#         json.dump(current_data, write_file)


# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help='echo the string you use here', type=int)
# args = parser.parse_args()
# print(args.echo**2)


# parser_2 = argparse.ArgumentParser()
# parser_2.add_argument('-v', '--verbosity', help='increase output verbosity', action='store_true')
# args_2 = parser_2.parse_args()
# if args_2.verbosity:
#     print('verbosity tured on')


# par = argparse.ArgumentParser()
# par.add_argument('square', type=int, help='display a square of given number')
# par.add_argument('-v', '--verbose', action="store_true", help='increase output verbosity')
# arg = par.parse_args()
# answer = arg.square**2
# if arg.verbose:
#     print("the square of {} equals {}".format(arg.square, answer))
# else:
#     print(answer)

def days_in_month(year, month):
    num_days = monthrange(year, month)[1]
    days = [date(year, month, day) for day in range(1, num_days + 1)]
    return days


d = days_in_month(2020, 3)
print(d[0])
