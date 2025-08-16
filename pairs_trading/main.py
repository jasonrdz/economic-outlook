# pandas for analysis
import pandas as pd

# system and operating system to help me grab some functions
import sys
import os

from functions.pairs_functions import * 
import matplotlib
matplotlib.use('Agg')  # <-- Add this before importing pyplot
import matplotlib.pyplot as plt

stocks = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "GOOGL", # Alphabet Inc. (Class A)
    "AMZN",  # Amazon.com Inc.
    "META",  # Meta Platforms Inc.
    "NVDA",  # NVIDIA Corporation
    "TSLA",  # Tesla Inc.
    "JPM",   # JPMorgan Chase & Co.
    "V",     # Visa Inc.
    "AMD", # AMD 
    "KO", # Coca Cola
    "SBUX", #Starbucks
    "PEP", # Pepsi
    "GE", # General Electric
    "GM", # General Motors
    "NFLX", # Netflix
    "RBLX", # Roblox
    "SONY", # Sony
    "WMT", # Walmart
    "IBM", # IBM
    "TGT", # target
    "COF" ,# Capital One,
    "PLTR", # Palantir,
    "MELI", # MercadoLibre
    "ROAD", #Construction
    "QUBT", # Quantum Computing
    "SHOP", # Shopify
    "ADBE" ,# Adobe
    "BRK-B",# berkshire hathaway
    "OKLO", # Oklo Inc
    "SMR" ,# Nuscale Power Corp
    # "FIG" # FIGMA 
]


data_dictionary = data_collecter(stocks)



stock_data, correlation = combining_stock_data(stocks)


correlated_stocks = identifying_pairs_stocks_highly_correlated(correlation)


stock_spread = calculating_spread(correlated_stocks, data_dictionary)


correlation_matrix = heatmap_of_correlation(correlation)


price_ratio_mean,z_ratio_score_graph,rolling_z_scores_mean = price_ratio_w_mean(stock_spread),z_score_ratio(stock_spread), rolling_avg_z_scores(stock_spread)


moving_average_bands = moving_average_zscore_bands(stock_spread)

strategy = buying_selling(stock_spread)

print(f'The Script has finished running.')