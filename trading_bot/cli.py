import argparse
import sys
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import setup_logger

# Initialize colorama
init(autoreset=True)

logger = setup_logger()

def print_header():
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*50}")
    print(f"{Fore.CYAN}{Style.BRIGHT}   Binance Futures Testnet Trading Bot CLI")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*50}\n")

def print_success(msg):
    print(f"{Fore.GREEN}[SUCCESS] {msg}")

def print_error(msg):
    print(f"{Fore.RED}[ERROR] {msg}")

def print_info(msg):
    print(f"{Fore.YELLOW}[INFO] {msg}")

def main():
    parser = argparse.ArgumentParser(description="Place orders on Binance Futures Testnet (USDT-M)")
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL", "buy", "sell"], help="Order side (BUY or SELL)")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "market", "limit"], help="Order type (MARKET or LIMIT)")
    parser.add_argument("--qty", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    print_header()

    # Validation
    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.qty)
        price = validate_price(args.price, order_type)
    except ValueError as e:
        print_error(f"Input Validation Failed: {e}")
        logger.error(f"Validation failed: {e}")
        sys.exit(1)

    print_info(f"Order Request Summary:")
    print(f"  - Symbol:   {symbol}")
    print(f"  - Side:     {side}")
    print(f"  - Type:     {order_type}")
    print(f"  - Quantity: {quantity}")
    if price:
        print(f"  - Price:    {price}")
    print()

    # Load environment variables
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print_error("BINANCE_API_KEY and BINANCE_API_SECRET must be set in .env file or environment variables.")
        sys.exit(1)

    # Initialize client and order manager
    try:
        print_info("Connecting to Binance Futures Testnet...")
        client = BinanceTestnetClient(api_key, api_secret)
        client.ping()
        print_success("Connected successfully.\n")
    except Exception as e:
        print_error("Failed to connect to Binance API. Check your credentials and network connection.")
        sys.exit(1)

    order_manager = OrderManager(client)

    # Execute Order
    print_info("Placing order...")
    result = order_manager.place_order(symbol, side, order_type, quantity, price)

    print()
    if result["success"]:
        print_success("Order placed successfully!")
        print(f"{Fore.GREEN}{Style.BRIGHT}--- Order Details ---")
        print(f"  Order ID:     {result['orderId']}")
        print(f"  Status:       {result['status']}")
        print(f"  Executed Qty: {result['executedQty']}")
        if result['avgPrice'] and float(result['avgPrice']) > 0:
            print(f"  Avg Price:    {result['avgPrice']}")
        print(f"{Fore.GREEN}{Style.BRIGHT}---------------------")
    else:
        print_error(f"Failed to place order.")
        print(f"Reason: {result['error']}")
        sys.exit(1)

if __name__ == "__main__":
    main()
