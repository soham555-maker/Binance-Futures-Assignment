from bot.client import BinanceTestnetClient
from bot.logging_config import setup_logger
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = setup_logger()

class OrderManager:
    def __init__(self, client: BinanceTestnetClient):
        self.client = client.get_client()

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """
        Place an order on Binance Futures Testnet.
        """
        logger.info(f"Preparing to place {order_type} order for {quantity} {symbol} ({side}).")
        
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        
        if order_type == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC' # Good Till Cancel
            
        try:
            logger.debug(f"Order API Request parameters: {params}")
            response = self.client.futures_create_order(**params)
            
            # Print response summary
            order_id = response.get('orderId')
            status = response.get('status')
            executed_qty = response.get('executedQty')
            avg_price = response.get('avgPrice')
            
            logger.info(f"Order placed successfully. Order ID: {order_id}")
            logger.debug(f"Full Order Response: {response}")
            
            return {
                "success": True,
                "orderId": order_id,
                "status": status,
                "executedQty": executed_qty,
                "avgPrice": avg_price,
                "raw_response": response
            }
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: Status Code {e.status_code}, Message: {e.message}")
            return {"success": False, "error": str(e)}
        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            return {"success": False, "error": "Network connection error."}
        except Exception as e:
            logger.error(f"Unexpected Error during order placement: {e}")
            return {"success": False, "error": "An unexpected error occurred."}
