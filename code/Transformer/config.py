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
    '1000BONKUSDT',
    '1000FLOKIUSDT',
    '1000PEPEUSDT',
    '1000SHIBUSDT',
    'AAVEUSDT',
    'ADAUSDT',
    'AGTUSDT',
    'AI16ZUSDT',
    'ALGOUSDT',
    'APTUSDT',
    'ARBUSDT',
    'ATOMUSDT',
    'AVAXUSDT',
    'B3USDT',
    'BCHUSDT',
    'BNBUSDT',
    'BROCCOLI714USDT',
    'BTCUSDT',
    'CFXUSDT',
    'CRVUSDT',
    'DOGEUSDT',
    'DOTUSDT',
    'DYDXUSDT',
    'EIGENUSDT',
    'ENAUSDT',
    'ENSUSDT',
    'ETCUSDT',
    'ETHFIUSDT',
    'ETHUSDT',
    'FARTCOINUSDT',
    'FETUSDT',
    'FILUSDT',
    'FLOWUSDT',
    'FUNUSDT',
    'GALAUSDT',
    'GASUSDT',
    'HBARUSDT',
    'HYPERUSDT',
    'HYPEUSDT',
    'ILVUSDT',
    'INJUSDT',
    'IPUSDT',
    'JTOUSDT',
    'JUPUSDT',
    'KERNELUSDT',
    'LDOUSDT',
    'LINKUSDT',
    'LTCUSDT',
    'MAGICUSDT',
    'MEMEUSDT',
    'MKRUSDT',
    'MOODENGUSDT',    
    'MYXUSDT',
    'NEARUSDT',
    'NEIROETHUSDT',
    'NEIROUSDT',
    'NEWTUSDT',
    'OGUSDT',
    'OMNIUSDT',
    'OMUSDT',
    'ONDOUSDT',
    'OPUSDT',
    'ORDIUSDT',
    'PARTIUSDT',
    'PENDLEUSDT',
    'PENGUUSDT',
    'PNUTUSDT',
    'POLUSDT',
    'POPCATUSDT',
    'RAREUSDT',
    'REDUSDT',
    'SAHARAUSDT',
    'SEIUSDT',
    'SKATEUSDT',
    'SOLUSDT',
    'SPKUSDT',
    'SPXUSDT',
    'SUIUSDT',
    'SUSDT',
    'SYNUSDT',
    'SYRUPUSDT',
    'TAOUSDT',
    'TIAUSDT',
    'TONUSDT',
    'TRUMPUSDT',
    'TRXUSDT',
    'UNIUSDT',
    'VINEUSDT',
    'VIRTUALUSDT',
    'WIFUSDT',
    'WLDUSDT',
    'XLMUSDT',
    'XRPUSDT',
    'XTZUSDT'
]


use_ticker_dict = {'CSI':USE_CSI_300_TICKET, 'TEST': USE_CSI_300_TICKET[:10]}

CSI_date = ['2025-07-07 13:30', '2025-07-26 00:00', '2025-07-24 00:00', '2025-08-01 00:00',  '2025-07-31 00:00', '2025-08-04 23:00']

date_dict = {'CSI': CSI_date, 'TEST': CSI_date}
