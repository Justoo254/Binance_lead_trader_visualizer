
---

## 📊 Example Insights

- Cleaned the three CSV data i.e the data containing OHLCV data from binance, data containing Lead traders position history and data containing the lead traders trade history
- Perfomed EDA on the data like Sharpe ratios, Mean PnL per trade, Longest position duration, Drawdown analysis etc 
- Visualizations e.g Line plot for Cumulative PnL, Histogram for PnL distribution
-Plotting the 1 month OHLCV data of ONDOUSDT symbol on a candlestick chart
-Overlaying entries and exits of ONDOUSDT trades on the candlestick chart to visualize strategy
-Added web analysis using plotly dash for non technical audience
## 🛠️ How to Run

1. Clone the repo  
   `git clone https://github.com/Justoo254/Binance_lead_trader_visualizer.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the notebooks 
   Open `notebooks/*.ipynb` in Jupyter Lab or VS Code.
4. Run Plotly app
  Open 'app.py' and run python3 app.py on the terminal to see the analysis via web
---

## 🔍 Disclaimer

This project is for **educational purposes only**. Data is scraped from publicly visible pages on Binance and does **not** violate any known terms of service. No financial advice is given.

---

## 📌 Future Work

- Add plotly dashboard for switching into multiple time frames for better entry and exit visualization
- Visualizing other symbols
- Compare multiple lead traders.

---

## 📬 Contact

If you find this useful or have ideas to expand it, feel free to reach out!
email: justookipkoech@gmail.com
Phone: +254727302216