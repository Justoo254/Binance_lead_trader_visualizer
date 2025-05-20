from scripts.clean_trade_history import clean_trade_history,clean_position_history
from scripts.merge_trades import merge_same_timestamp_trades
import pandas as pd

df_position_history = clean_position_history("data/lead_trader_9m_ph.csv")
df_position_history = df_position_history.sort_values(["Closed Time", "Opened Time"])
df_position_history = df_position_history.reset_index(drop=True)
df_position_history["Cumulative PnL"] = df_position_history["Closing PnL (USDT)"].cumsum()
df_position_history["Running Max"] = df_position_history["Cumulative PnL"].cummax()
df_position_history["Drawdown"] =df_position_history["Cumulative PnL"]-df_position_history["Running Max"]


df_1000pepeusdt_ohlcv = pd.read_csv("data/1000pepeusdt_2025-01-27_00-00-00_2025-03-21_23-59-59.csv", parse_dates=["timestamp"])
df_trade_history = clean_trade_history("data/lead_trader_2m_th.csv")

# Make timestamps timezone-aware

df_1000pepeusdt_ohlcv["timestamp"] = pd.to_datetime(df_1000pepeusdt_ohlcv["timestamp"], utc=True)
df_1000pepeusdt_ohlcv = df_1000pepeusdt_ohlcv[
    df_1000pepeusdt_ohlcv["timestamp"] <= pd.to_datetime("2025-03-21 23:59:59", utc=True)
]
df_1000pepeusdt_ohlcv["timestamp"] += pd.Timedelta(hours=3)
# subset to only 1000PEPEUSDT trades
df_1000PEPEUSDT= df_trade_history[df_trade_history["Symbol"] == "1000PEPEUSDT"]
df_1000PEPEUSDT = merge_same_timestamp_trades(df_1000PEPEUSDT)
df_1000PEPEUSDT["Time"] = df_1000PEPEUSDT["Time"].dt.tz_convert("Etc/GMT")
# ✅ Load and clean position history
df_position_history = clean_position_history("data/lead_trader_9m_ph.csv")
df_position_history = df_position_history.sort_values(["Closed Time", "Opened Time"])
df_position_history = df_position_history.reset_index(drop=True)
df_position_history["Cumulative PnL"] = df_position_history["Closing PnL (USDT)"].cumsum()
df_position_history["Running Max"] = df_position_history["Cumulative PnL"].cummax()
df_position_history["Drawdown"] =df_position_history["Cumulative PnL"]-df_position_history["Running Max"]
__all__ = ['df_position_history','df_1000pepeusdt_ohlcv', 'df_1000PEPEUSDT']
