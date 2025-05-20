import pandas as pd
def clean_trade_history(filepath):
    #Rename cols
    df_trade_history = pd.read_csv(filepath)
    df_trade_history=df_trade_history.drop(columns= "Column3")
    df_trade_history = df_trade_history.rename(columns={
        "Column1":"Time",
        "Column2":"Symbol",
        "Column4":"Side",
        "Column5":"Price",
        "Column6": "Quantity",
        "Column7": "Realized Profit(USDT)"
    })
    df_trade_history["Realized Profit(USDT)"] = round(df_trade_history["Realized Profit(USDT)"].str.replace("USDT", "", regex=False).astype(float),2)
    df_trade_history["Quantity"]=[float(val.split()[0].replace(",","")) for val in df_trade_history["Quantity"]]
    df_trade_history["Symbol"]= df_trade_history["Symbol"].str.replace("Perp", "", regex=False)
    df_trade_history["Time"] = pd.to_datetime(df_trade_history["Time"], utc=True)
    df_trade_history = df_trade_history.drop_duplicates()
    #Subset to chosen symbol
    return df_trade_history

def clean_position_history(filepath):
    df_position_history = pd.read_csv(filepath)
    #Rename columns
    
    # Clean columns by removing "USDT" and stripping spaces, then convert to float
    cols_to_clean = ["Entry Price", "Closing PNL", "Avg Close Price"]
    df_position_history[cols_to_clean] = df_position_history[cols_to_clean].apply(
        lambda col: col.str.replace("USDT", "").str.strip()
    ).astype(float)

    # Rename columns 
    df_position_history = df_position_history.rename(columns={
        "Entry Price": "Entry Price (USDT)",
        "Avg Close Price": "Avg Close Price (USDT)",
        "Closing PNL": "Closing PnL (USDT)"
    })
    #Convert Closed Time & Closed Time to date time
    df_position_history["Opened Time"] = pd.to_datetime(df_position_history["Opened Time"])
    df_position_history["Closed Time"] = pd.to_datetime(df_position_history["Closed Time"])
    df_position_history = df_position_history[["Symbol","Opened Time", "Entry Price (USDT)", "Closing PnL (USDT)", "Closed Time","Avg Close Price (USDT)"]]
    return df_position_history