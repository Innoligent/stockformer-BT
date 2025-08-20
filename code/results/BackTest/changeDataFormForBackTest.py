# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 16:01:48 2025

@author: Fieldyy
"""

import pandas as pd
import datetime

path = 'positionWeight_normWeight.csv'

def utc_to_unix(utc_str, fmt="%Y/%m/%d %H:%M"):
    dt = datetime.datetime.strptime(utc_str, fmt)
    dt_utc = dt.replace(tzinfo=datetime.timezone.utc)
    return int(dt_utc.timestamp())

if 1:
    df = pd.read_csv(path)
    df['signal_time'] = df['date'].apply(utc_to_unix)
    
    coin_pool = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT']
    result = []
    for coin in coin_pool:
        df_temp = df[['signal_time',coin]].copy()
        df_temp['symbol'] = coin
        df_temp.rename(columns={coin:'position'},inplace=True)
        result.append(df_temp)
    df_result = pd.concat(result, ignore_index=True)
    df_result.to_parquet('position_weight_for_alpha_backtest.parquet')
