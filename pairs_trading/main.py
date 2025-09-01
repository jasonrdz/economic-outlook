# pandas for analysis
import pandas as pd

# system and operating system to help me grab some functions
import sys
import os
import requests
from io import StringIO


from functions.pairs_functions import * 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
html = StringIO(response.text)

tables = pd.read_html(html)
df = tables[0]  
stocks = df['Symbol'].tolist()

stocks = list(set(stocks))


stocks = [stock for stock in stocks if stock.lower() not in ('brk.b', 'bf.b')]



data_dictionary = data_collecter(stocks)



stock_data, correlation = combining_stock_data(stocks)


correlated_stocks = identifying_pairs_stocks_highly_correlated(correlation)


stock_spread = calculating_spread(correlated_stocks, data_dictionary)


correlation_matrix = heatmap_of_correlation(correlation)


price_ratio_mean,z_ratio_score_graph,rolling_z_scores_mean = price_ratio_w_mean(stock_spread),z_score_ratio(stock_spread), rolling_avg_z_scores(stock_spread)


moving_average_bands = moving_average_zscore_bands(stock_spread)

strategy = buying_selling(stock_spread)

print(f'The Script has finished running.')