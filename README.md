#  Binance Futures Testnet Trading Bot

##  Overview

This is a Python-based CLI trading bot that interacts with Binance Futures Testnet. It allows users to place MARKET and LIMIT orders with proper validation, logging, and error handling.

---

##  Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Structured logging (request, response, errors)
* Exception handling for API and validation errors

---

##  Tech Stack

* Python 3.x
* python-binance
* argparse
* dotenv

---

##  Project Structure

```
binance-trading-bot/
│── app/
│   ├── client.py
│   ├── trading.py
│   ├── logger.py
│── main.py
│── requirements.txt
│── README.md
│── logs/
│   └── bot.log
```

---

##  Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd binance-trading-bot
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create `.env` file

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
```

---

##  Usage

###  MARKET Order

```
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

###  LIMIT Order

```
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

---

##  Sample Output

```
=== ORDER RESPONSE ===
Order ID: 123456
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00

 Order placed successfully
```

---

## Logs

Logs are stored in:

```
logs/bot.log
```

Example:

```
INFO - Request: {...}
INFO - Response: {...}
ERROR - Error: ...
```

---

##  Important Notes

* Uses Binance Futures Testnet
* Minimum order notional must be ≥ 50 USDT
* MARKET orders may remain in NEW state due to testnet liquidity

---

##  Future Improvements

* Add Stop Loss / Take Profit
* Add leverage control
* Add order tracking
* Add retry logic for API failures

---

## Author

Maithili Burghate
