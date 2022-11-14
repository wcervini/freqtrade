from backtesting import Backtest, Strategy
import pandas_datareader as pdr
import yfinance as yf
import ccxt

from datetime import datetime
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
binance = ccxt.binance()

data = binance.fetch_ohlcv(symbol="ADA/USDT",timeframe="15m" )



    
    
    