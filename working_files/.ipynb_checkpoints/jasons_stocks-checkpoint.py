import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, date
import pandas_datareader.data as web
import statistics as stats
import mplfinance as mpf
import os
import sys
sys.path.append('./working_files')
from working_files.functions import *

#############################################################################################################
#############################################################################################################
year = int(2025)

apple_info, apple = finding_stock_info('AAPL', year)
google_info, google = finding_stock_info('GOOGL',year)
dfs_info, dfs = finding_stock_info('DFS',year)
star_info, starbucks = finding_stock_info('SBUX',year)
spy_info, spy = finding_stock_info('SPY',year)
netflix_info, netflix = finding_stock_info('NFLX',year)
qqq_info, qqq = finding_stock_info('QQQ',year)
vix_info, vix = finding_stock_info('^VIX',year)
meta_info, meta = finding_stock_info('META',year)
nvidia_info, nvidia = finding_stock_info('NVDA',year)
coke_info, coke = finding_stock_info('KO',year)
voo_info, voo = finding_stock_info('VOO', year)

# this is necessary for on-going work and insights
apple = adding_relevant_columns(apple)
google = adding_relevant_columns(google)
discover = adding_relevant_columns(dfs)
qqq = adding_relevant_columns(qqq)
starbucks = adding_relevant_columns(starbucks)
netflix = adding_relevant_columns(netflix)
spy = adding_relevant_columns(spy)
vix = adding_relevant_columns(vix)
meta = adding_relevant_columns(meta)
nvidia = adding_relevant_columns(nvidia)
coke = adding_relevant_columns(coke)
voo = adding_relevant_columns(voo)

#############################################################################################################
#############################################################################################################



tracking(qqq, 'QQQ')
tracking(spy, 'SPY')
tracking(nvidia, 'NVDA')
tracking(netflix, 'NFLX')
tracking(apple, 'AAPL')
tracking(google, 'GOOG')
tracking(voo, 'VOO')





#############################################################################################################
 #############################################################################################################

