from dash import Dash, html, dcc, callback, Output, Input, State
# from scripts.update_chart import update_chart, df_1000PEPEUSDT,df_1000pepeusdt_ohlcv
import plotly.express as px
from scripts.data_loader import  df_1000PEPEUSDT,df_1000pepeusdt_ohlcv,df_position_history
from scripts.update_charts_web import update_chart,plot_drawdown, line_plot, plot_hist,bar_plot
app = Dash(__name__)
WINDOW_SIZE=200
start_index=0
app.layout = html.Div([
    html.Div([
        html.H2("Analysis of the position data",style={'textAlign': 'center'}),
        html.H3("Drawdown plot"),
        html.P("Chart showed deep drawdowns experienced near the end of Dec 2024 and at the beginning of march 2025."),
        dcc.Graph(id='drawdown-plot', figure=plot_drawdown(df_position_history)),
        html.H3("Line plot for cumulative pnl"),
        html.P("The line plot of the cumulative pnl showed a steady return up to mid November 2024 where it rose sharply. Notice the sharp drawdowns on December 2024 and at the beginning of March 2025"),
        dcc.Graph(id='line-plot', figure=line_plot(df_position_history)),
        html.H3("Histogram for distribution of profit and losses"),
        html.P("- Most trades are centered around zero meaning the lead trader closes at small profits and losses."),
        html.P("- Slight right skew."),
        html.P("-There are more frequent small gains, but some outliers exist on both ends."),
        html.P("-The right tail (positive PnL) is longer, showing that while most gains are small, a few large positive trades occurred."),
        dcc.Graph(id='hist-plot', figure=plot_hist(df_position_history)),
        html.H3("Horizontal barchart to visualize number of positions per symbol"),
        html.P("The most traded symbol was ONDOUSDT for the period."),
        dcc.Graph(id='bar-plot', figure=bar_plot(df_position_history))
        
    ]),
    html.H1('Interactive Candlestick Chart', style={'textAlign': 'center'}),
    
    dcc.Store(id='window-start', data=start_index),  # Store the current window start index
    
    html.Div([
        html.Button("Left", id="btn-left", n_clicks=0),
        html.Button("Right", id="btn-right", n_clicks=0),
    ], style={'textAlign': 'center', 'marginBottom': 20}),
    
    dcc.Graph(id='candlestick-chart')
])
@app.callback(
    Output('candlestick-chart', 'figure'),
    Output('window-start', 'data'),
    Input('btn-left', 'n_clicks'),
    Input('btn-right', 'n_clicks'),
    State('window-start', 'data')
)
def call_update_chart(n_clicks_left, n_clicks_right, window_start):
    if window_start is None:     
        window_start = 0
    return update_chart(n_clicks_left, n_clicks_right, window_start, WINDOW_SIZE, df_1000PEPEUSDT, df_1000pepeusdt_ohlcv)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8052)
