import pandas as pd
def merge_same_timestamp_trades(df_1000PEPEUSDT):
    # df_1000PEPEUSDT = df_1000PEPEUSDT.copy()
    merged_rows = []
    i = 0
    df_1000PEPEUSDT = df_1000PEPEUSDT.sort_values("Time").reset_index(drop=True)

    while i < len(df_1000PEPEUSDT):
        current_time = df_1000PEPEUSDT.iloc[i]["Time"]
        
        # Filter rows within 30 seconds window of current_time
        same_time_rows = df_1000PEPEUSDT[
            (df_1000PEPEUSDT["Time"] >= current_time) & 
            (df_1000PEPEUSDT["Time"] <= current_time + pd.Timedelta(seconds=30))
        ]

        if len(same_time_rows) > 1:
            # Create a merged row by summing the quantities and realized profit
            merged_row = same_time_rows.iloc[0].copy()
            merged_row["Quantity"] = same_time_rows["Quantity"].sum()
            merged_row["Realized Profit(USDT)"] = same_time_rows["Realized Profit(USDT)"].sum()
            merged_rows.append(merged_row)
            
            # Skip over the rows that have been merged
            i += len(same_time_rows)
        else:
            # If there's only one row for this timestamp, append it as is
            merged_rows.append(df_1000PEPEUSDT.iloc[i])
            i += 1

    # Return the DataFrame with merged rows
    df_1000PEPEUSDT_merged = pd.DataFrame(merged_rows).reset_index(drop=True)
    return df_1000PEPEUSDT_merged
    