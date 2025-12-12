# pandas for analysis
import pandas as pd

# system and operating system to help me grab some functions
import sys
import os
import requests
from io import StringIO
import time
from functions.pairs_functions import * 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

html = 'https://www.slickcharts.com/sp500'

sp500_tickers = []
response = pd.read_html(html)
table = pd.read_html(html)[0]


for stock in table['Symbol']:
    if stock == 'BRK.B' or stock == 'BR.B' or stock  == 'BR.F' or stock == 'BF.B':
        continue
    sp500_tickers.append(stock)
    
        
stocks = list(set(sp500_tickers))


# stocks = [stock for stock in stocks if stock.lower() not in ('brk.b', 'bf.b')]



data_dictionary = data_collecter(stocks)



stock_data, correlation = combining_stock_data(stocks)


correlated_stocks = identifying_pairs_stocks_highly_correlated(correlation)


stock_spread = calculating_spread(correlated_stocks, data_dictionary)


correlation_matrix = heatmap_of_correlation(correlation)


price_ratio_mean,z_ratio_score_graph,rolling_z_scores_mean = price_ratio_w_mean(stock_spread),z_score_ratio(stock_spread), rolling_avg_z_scores(stock_spread)


moving_average_bands = moving_average_zscore_bands(stock_spread)

strategy = buying_selling(stock_spread)

print(f'The Script has finished running.')