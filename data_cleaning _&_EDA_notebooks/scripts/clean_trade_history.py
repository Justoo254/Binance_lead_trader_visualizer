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

    return df_trade_history