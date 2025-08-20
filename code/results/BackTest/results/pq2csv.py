import pandas as pd

# 读取 parquet 文件
df = pd.read_parquet("position_weight_normWeight_return_5min.parquet")

# 保存为 csv 文件
df.to_csv("position_weight_for_alpha_backtest_return_5min.csv", index=False)
