"""
strategy.py
Defines the momentum breakout + volume confirmation trading logic.
"""
import pandas as pd

def generate_signals(df: pd.DataFrame, lookback: int = 20, vol_window: int = 20) -> pd.DataFrame:
    """
    Generate buy/sell signals based on breakout and volume confirmation.
    Args:
        df (pd.DataFrame): Price and volume data.
        lookback (int): Lookback window for breakout.
        vol_window (int): Window for average volume.
    Returns:
        pd.DataFrame: DataFrame with signal columns ['buy_signal', 'sell_signal']
    """
    # Ensure all columns are Series (fixes yfinance MultiIndex/alignment issue)
    close  = df['Close'].squeeze()
    high   = df['High'].squeeze()
    volume = df['Volume'].squeeze()

    signals = pd.DataFrame(index=df.index)
    signals['rolling_high'] = high.rolling(lookback).max()
    signals['avg_volume']   = volume.rolling(vol_window).mean()

    signals['buy_signal'] = (
        (close > signals['rolling_high'].shift(1)) &
        (volume > signals['avg_volume'])
    )
    signals['sell_signal'] = False  # Sell handled by backtest (trailing stop/MA)
    return signals[['buy_signal', 'sell_signal']]