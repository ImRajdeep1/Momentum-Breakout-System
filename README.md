# Momentum Breakout Trading System with Visual Analytics

A Python-based algorithmic trading system that captures strong trends 
using breakout and volume confirmation logic.

## Features
- Automated buy/sell signal generation (breakout + volume confirmation)
- Backtesting with realistic trade simulation
- Performance metrics (Total Return, Sharpe Ratio, Max Drawdown)
- Dark-themed visual analytics (Price, Equity Curve, Volume)

## Backtest Results — TCS.NS (Jan 2024 – Jan 2025)

| Metric | Value |
|---|---|
| Total Return | 935.06% |
| Sharpe Ratio | 6.18 |
| Max Drawdown | -1.73% |

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ImRajdeep1/Momentum-Breakout-System.git
```

### 2. Install dependencies
```bash
pip install yfinance pandas numpy matplotlib
```

### 3. Run the project
Open `main.py` in Spyder and press F5.

Change the symbol inside `main.py`:
```python
SYMBOL = 'TCS.NS'        # NSE: TCS.NS, RELIANCE.NS, INFY.NS
START  = '2024-01-01'
END    = '2025-01-01'
```

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — runs the full pipeline |
| `data.py` | Fetches real or simulated price data via yfinance |
| `strategy.py` | Momentum breakout + volume confirmation signal logic |
| `backtest.py` | Trade simulation, trailing stop, and performance metrics |
| `visualization.py` | Dark-themed chart generation (Price, Equity, Volume) |

## Tech Stack
Python | pandas | NumPy | matplotlib | yfinance

## References
- [Breakout (Technical Analysis)](https://en.wikipedia.org/wiki/Breakout_(technical_analysis))
- [Momentum (Finance)](https://en.wikipedia.org/wiki/Momentum_(finance))
- [Sharpe Ratio](https://en.wikipedia.org/wiki/Sharpe_ratio)
- [Drawdown (Economics)](https://en.wikipedia.org/wiki/Drawdown_(economics))
