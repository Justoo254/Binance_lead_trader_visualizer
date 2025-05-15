# Function to find the closest 5-minute candlestick
def find_nearest_candle(trade_time, df):
    return df.iloc[(df["timestamp"] - trade_time).abs().idxmin()]

# Plot entry trades
for _, trade in entries_df.iterrows():
    nearest_candle = find_nearest_candle(trade["Timestamp"], df)
    
    fig.add_trace(go.Scatter(
        x=[nearest_candle["timestamp"]],
        y=[trade["Price"]],
        mode="markers",
        marker=dict(color="blue", size=8, symbol="triangle-up"),
        name=f"Entry: {trade['Timestamp'].strftime('%H:%M')}"
    ))

