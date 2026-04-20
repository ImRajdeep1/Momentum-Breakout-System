"""
main.py
Orchestrates the trading system: loads data, runs strategy, backtests, visualizes, and outputs results.
"""
import sys
import pandas as pd
from datetime import datetime, timedelta
from data import fetch_data
from strategy import generate_signals
from backtest import run_backtest, calculate_metrics
from visualization import plot_all

if __name__ == "__main__":

    SYMBOL   = 'TCS.NS'
    START    = '2024-01-01'
    END      = '2026-01-01'
    SIMULATE = False

    print(f"Fetching data for {SYMBOL}...")
    df = fetch_data(SYMBOL, START, END, simulate=SIMULATE)

    print("Generating signals...")
    signals = generate_signals(df)

    print("Running backtest...")
    equity_df, trades = run_backtest(df, signals)
    equity_curve = equity_df['equity_curve']

    print("Calculating metrics...")
    metrics = calculate_metrics(equity_curve)

    print("\nPerformance Summary:")
    for k, v in metrics.items():
        print(f"  {k}: {v}")

    print("\nTrade Log:")
    print(trades.to_string(index=False))

    print("\nPlotting results...")
    plot_all(df, signals, trades, equity_curve)