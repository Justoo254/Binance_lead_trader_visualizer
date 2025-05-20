#Importing required libraries
import requests
import pandas as pd
import time
from datetime import datetime, timedelta, timezone
def fetch_symbol(symbol, start_time, end_time):
    # Convert start and end timestamps to milliseconds
    start_time_ms = int(datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).timestamp() * 1000)
    end_time_ms = int(datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).timestamp() * 1000)
    
    all_data = []
    LIMIT = 1500
    interval = "5m"
    BASE_URL = "https://fapi.binance.com/fapi/v1/klines"
    
    print(f"Fetching {symbol} {interval} data from {start_time} to {end_time}...")
    print(f"Limit: {LIMIT}") 
    while start_time_ms < end_time_ms:
        params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": start_time_ms,
            "limit": LIMIT
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if not data:
            print("No more data found.")
            break

        all_data.extend(data)
        print(f"Limit:{LIMIT}")
        # Update start_time_ms to one millisecond after the last fetched candle
        start_time_ms = int(data[-1][0]) + 1

        # To avoid hitting Binance rate limits
        time.sleep(0.5)

    # Convert to DataFrame
    df = pd.DataFrame(all_data, columns=[
        "timestamp", "open", "high", "low", "close", "volume", 
        "close_time", "quote_asset_volume", "trades", "taker_base", "taker_quote", "ignore"
    ])

    # Convert timestamp to readable datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    return df
