import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
def plot_candlesticks(df, symbol="100PEPEUSDT", interval="5M"):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df["timestamp"],
            open=df["open"],
            close=df["close"],
            high=df["high"],
            low=df["low"],
            increasing=dict(line=dict(color="green")),
            decreasing=dict(line=dict(color="red"))
        )
    ])

    fig.update_layout(
        title=f"Candlestick chart for {symbol}-{interval} interval",
        width=2000,
        hovermode="x",
        # template="plotly_dark",
        xaxis=dict(rangeslider=dict(visible=False)),
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig  # Return the figure to keep it chainable

#Helper function
def find_enclosing_candle(trade_time, df_ohlcv):
    """
    Find the candle that contains the trade time — i.e., the latest candle
    at or before the trade time.
    
    Assumes df_ohlcv["timestamp"] is sorted in ascending order.
    """
    mask = df_ohlcv["timestamp"] <= trade_time
    if mask.any():
        return df_ohlcv[mask].iloc[-1]
    else:
        return None  # Handle edge case: trade before any candle

def plot_entry_trades(fig, entries_df,exits_df,df_1000pepeusdt_ohlcv):
    """
    Adds entry trade markers to a Plotly figure.

    Parameters:
        fig (go.Figure): Existing Plotly figure to add to.
        entries_df (pd.DataFrame): DataFrame with entry trades. Requires 'Timestamp' and 'Price' columns.
        df_ohlcv (pd.DataFrame): OHLCV data with a 'timestamp' column.
    """
    for _, trade in entries_df.iterrows():
        nearest_candle = find_enclosing_candle(trade["Time"], df_1000pepeusdt_ohlcv)

        fig.add_trace(go.Scatter(
            x=[nearest_candle["timestamp"]],
            y=[trade["Price"]],
            mode="markers",
            marker=dict(color="blue", size=8, symbol="triangle-up"),
            name=f"Entry: {trade['Time'].strftime('%H:%M')}"
        ))
    # Plot exit trades
    for _, trade in exits_df.iterrows():
        nearest_candle = find_enclosing_candle(trade["Time"], df_1000pepeusdt_ohlcv)
        
        fig.add_trace(go.Scatter(
            x=[nearest_candle["timestamp"]],
            y=[trade["Price"]],
            mode="markers",
            marker=dict(color="orange", size=8, symbol="triangle-down"),
            name=f"Exit: {trade['Time'].strftime('%H:%M')}"
        ))

    return fig  # Again, return the modified figure

