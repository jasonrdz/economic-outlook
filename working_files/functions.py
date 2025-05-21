import pandas as pd
import os
import numpy as np
import requests
from fredapi import Fred
import json
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, date
import pandas_datareader.data as web
import statistics as stats
import mplfinance as mpf

def format_date(date_string):
    try:
        month_number, year = date_string.split("-")
        month_name = datetime.strptime(month_number, "%m").strftime("%b")
        return f"{month_name} {year}"
    except ValueError:
        return "Invalid date format"

def finding_stock_info(ticker, beginning_year):
    year = int(beginning_year)
    stock = yf.Ticker(ticker)
    start = datetime(2020, 1, 1)
    end = date.today()
    
    stock_info = stock.info
    historical_data = stock.history(start=start, end=end)
    
    return stock_info, historical_data

def stock_insights(ticker):
    # market cap, determines company's value given their opening price times
    # volume traded
    ticker['market_cap'] = ticker['Open'] * ticker['Volume']
    # daily return 
    # ((Today's Closing Price - Yesterday's Closing Price) 
    # / Yesterday's Closing Price) * 100
    ticker['daily_return'] = ((ticker['Close'] - ticker['Close'].shift(1)) / ticker['Close'].shift(1)) * 100

    return ticker

def finding_stock_info(ticker, starting_year):
    year = int(starting_year)
    stock = yf.Ticker(ticker)
    start = datetime(year, 1, 1)
    end = date.today()
    
    stock_info = stock.info
    historical_data = stock.history(start=start, end=end)
    
    return stock_info, historical_data

def adding_relevant_columns(stock):
    # market cap is relevant given there is a measurement of the company's size
    stock['market_cap'] = stock['Open'] * stock['Volume']
    # daily return
    stock['daily_return'] = ((stock['Close'] - stock['Close'].shift(1)) 
                             / stock['Close'].shift(1)) * 100
    # calculating moving_average
    moving_window = 30
    stock['moving_average'] = stock['Close'].rolling(window=moving_window, min_periods=1).mean()


    # adding in a ema tracker


    stock['ema'] = stock['Close'].ewm(span=50, adjust=False).mean()


    return stock


def closing_price(*tickers, labels=None):
    if labels is None:
        labels = [f'Stock {i+1}' for i in range(len(tickers))]

    plt.figure(figsize=(12, 6))

    for df, label in zip(tickers, labels):
        df['Close'].plot(label=label)

    plt.xlabel('Time Horizon')
    plt.ylabel('Closing Price of Stocks in Hundreds')
    plt.title('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    return plt.show()


def tracking(stock, stock_string):
    stock['Close'].plot()
    stock['moving_average'].plot()
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.title(f'closing price and moving average for {stock_string}')
    folder = 'working_files/moving_averages'
    os.makedirs(folder, exist_ok=True)
    plt.savefig(f'{folder}/{stock_string}.png')
    return plt.show()
    


def moving_average(df, time_period):
    gdp_data = df['gdp_per_capita'].values
    data = []
    data_together = []
    for item in gdp_data:
        data.append(item)
        if len(data) > time_period:
            del(data[0])
        data_together.append(round(stats.mean(data),0))

    df[f'moving_average_across_{time_period}_years'] = pd.Series(data_together, df.index)
    return df




