import duckdb as duck
from openbb import obb
import polars as pl

import os
os.chdir('..')
print(os.getcwd())
import sys 
sys.path.append('./working_files/')
from functions import *



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
    "SMR" # Nuscale Power Corp
]


con = duck.connect('./database/stocks.db')

all_data = []

for stock in stocks:
    stock_data = adding_relevant_columns(
        obb.equity.price.historical(
            symbol=stock,
            provider='yfinance',
            start_date='2007-01-01'
        ).to_df()
    )
    pl_df = (
        pl.from_pandas(stock_data.reset_index())
        .with_columns([pl.lit(stock).alias("Symbol")])
    )
    all_data.append(pl_df)



for i, df in enumerate(all_data):
    print(f"DataFrame {i}: {df.columns}")
# Concatenate all Polars DataFrames
# data_read = pl.concat(all_data)

# data_read


# con.execute('CREATE TABLE IF NOT EXISTS stock_overview as SELECT * FROM data_read')

# for i, df in enumerate(all_data):
#     print(f"DataFrame {i}: {df.columns}")
    





# print(pl.from_pandas(con.execute('Select * from stock_overview').fetchdf()))
