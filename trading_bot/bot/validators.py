def validate_symbol(symbol: str) -> str:
    symbol = symbol.upper()
    if not symbol.isalnum():
        raise ValueError("Symbol must be alphanumeric (e.g., BTCUSDT).")
    return symbol

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return quantity

def validate_price(price: float, order_type: str) -> float:
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders.")
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0.")
    return price
