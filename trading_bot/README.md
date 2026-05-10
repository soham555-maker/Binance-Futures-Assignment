# Binance Futures Testnet Trading Bot

A simplified, structured Python CLI application to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Features

- **Order Types:** Place MARKET and LIMIT orders.
- **Validation:** Input validation for symbol, side, order type, quantity, and price.
- **Error Handling:** Graceful handling of API errors and network issues.
- **Logging:** Structured logging to both console and a log file (`trading_bot.log`).
- **Enhanced CLI UX:** Clean output formatting with color coding.

## Prerequisites

- Python 3.8+
- Binance Futures Testnet account.
- API Key and API Secret from the testnet dashboard.

## Setup Instructions

1. **Clone or Extract the Project:**
   ```bash
   git clone <your-repo-link>
   cd trading_bot
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Rename `.env.example` to `.env` and fill in your testnet credentials.
   ```
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_api_secret_here
   ```

## How to Run Examples

Use the `cli.py` entry point to place orders.

**View Help:**
```bash
python cli.py --help
```

**1. Place a MARKET BUY order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```

**2. Place a LIMIT SELL order:**
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 65000.50
```

## Logging

All API requests, responses, and errors are logged to `trading_bot.log`. Check this file for detailed debug information if an order fails.

## Assumptions

- **Leverage:** The bot assumes leverage is already set via the Binance UI or defaults to the account's existing leverage. It does not actively manage leverage.
- **Margin Type:** Cross/Isolated margin settings rely on the account's default.
- **Testnet:** The bot operates **only** on the Binance Futures Testnet. Do not use production API keys.
