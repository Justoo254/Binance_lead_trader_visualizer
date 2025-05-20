from scripts.plot_candlesticks import plot_candlesticks, plot_entry_trades
import plotly.express as px
def update_chart(n_clicks_left, n_clicks_right, window_start, WINDOW_SIZE,  df_trades,df_ohlcv):
    move = n_clicks_right - n_clicks_left
    new_start = window_start + move * WINDOW_SIZE
    max_start = len(df_ohlcv) - WINDOW_SIZE

    new_start = max(0, min(new_start, max_start))
    window_df = df_ohlcv.iloc[new_start:new_start + WINDOW_SIZE]

    start_ts = window_df["timestamp"].min()
    end_ts = window_df["timestamp"].max()

    filtered_trades = df_trades[(df_trades["Time"] >= start_ts) & (df_trades["Time"] <= end_ts)]
    entries_df = filtered_trades[filtered_trades["Side"] == "Open long"]
    exits_df = filtered_trades[filtered_trades["Side"] == "Close long"]

    fig = plot_candlesticks(window_df, symbol="1000PEPEUSDT", interval="5M")
    fig = plot_entry_trades(fig, entries_df, exits_df, window_df)
    return fig, new_start
def plot_drawdown(df_position_history):
    fig = px.line(df_position_history, x="Closed Time", y="Drawdown", title="Drawdown Over Time",color_discrete_sequence=["red"])
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Drawdown(USDT)",
        
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        width=1200,   
        height=500
    )

    return fig
def line_plot(df_position_history):
    fig=px.line(df_position_history, x="Closed Time", y="Cumulative PnL", title="Cumulative PnL Over Time")
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Cumulative PnL (USDT)", 
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        width=1000,
        height=500
    )
    return fig
def plot_hist(df_position_history):
    fig = px.histogram(
        df_position_history,
        x="Closing PnL (USDT)",
        nbins=30,
        title="PnL Distribution"
    )

    fig.update_traces(
        marker=dict(
            color='skyblue',
            line=dict(
                color='black',  
                width=1                     )
        )
    )

    fig.update_layout(
        xaxis_title="PnL (USDT)",
        yaxis_title="Number of Positions",
        width=800,
        height=500
    )
    return fig
def bar_plot(df_position_history):
    no_positions_per_symbol = df_position_history["Symbol"].value_counts()
    top_10=no_positions_per_symbol.head(10)
    fig = px.bar(
        top_10,
        x=top_10.values,
        y=top_10.index,
        orientation='h',
        labels={'x': 'Number of Positions', 'y': 'Symbol'},
        title='Top 10 Symbols by Number of Positions',
        color_discrete_sequence=['skyblue']
    )

    fig.update_layout(
        width=800,
        height=500,
        yaxis=dict(autorange="reversed")  
    )

    return fig
