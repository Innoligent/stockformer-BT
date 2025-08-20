START_DATE = "2025-07-06 06:20"
END_DATE = "2025-08-05 08:15"

INF = 1100

## stockstats technical indicator column names
## check https://pypi.org/project/stockstats/ for different names
TECHNICAL_INDICATORS_LIST = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
    # "return_ratio",
]


ADDITIONAL_FEATURE = [
    'label_short_term',
    'label_long_term'
]

TEMPORAL_FEATURE = [
    'open', 
    'close', 
    'high', 
    'low', 
    'volume', 
    'dopen', 
    'dclose', 
    'dhigh', 
    'dlow', 
    'dvolume'
]


# use CSI -300 ticker
USE_CSI_300_TICKET = [
   'BTCUSDT',
   'ETHUSDT',
   'SOLUSDT',
]


use_ticker_dict = {'CSI':USE_CSI_300_TICKET, 'TEST': USE_CSI_300_TICKET[:2]}

CSI_date = ['2025-07-07 13:30', '2025-07-26 00:00', '2025-07-24 00:00', '2025-08-01 00:00',  '2025-07-31 00:00', '2025-08-04 23:00']

date_dict = {'CSI': CSI_date, 'TEST': CSI_date}
