"""
data.py
Fetches or simulates historical price and volume data for the trading system.
"""
import pandas as pd
import numpy as np

def fetch_data(symbol: str, start: str, end: str, simulate: bool = False) -> pd.DataFrame:
    if simulate:
        np.random.seed(42)
        dates = pd.date_range(start, end)
        price = np.cumprod(1 + np.random.normal(0, 0.01, len(dates))) * 100
        volume = np.random.randint(1e5, 2e5, len(dates))
        df = pd.DataFrame({
            'Open': price * (1 + np.random.normal(0, 0.002, len(dates))),
            'High': price * (1 + np.random.normal(0.01, 0.005, len(dates))),
            'Low': price * (1 - np.random.normal(0.01, 0.005, len(dates))),
            'Close': price,
            'Volume': volume
        }, index=dates)
        return df
    else:
        try:
            import yfinance as yf
        except ImportError:
            raise ImportError("yfinance not installed.")

        df = yf.download(symbol, start=start, end=end, auto_adjust=True)

        # Fix for yfinance MultiIndex columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if df.empty:
            raise ValueError("No data fetched. Check symbol and date range.")

        return df[['Open', 'High', 'Low', 'Close', 'Volume']]