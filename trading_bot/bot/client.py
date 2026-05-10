from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceTestnetClient:
    def __init__(self, api_key: str, api_secret: str):
        if not api_key or not api_secret:
            raise ValueError("API Key and Secret must be provided.")
        
        logger.info("Initializing Binance Futures Testnet Client.")
        # Setup client, use testnet for futures
        self.client = Client(api_key, api_secret, testnet=True)
        
    def ping(self):
        try:
            logger.debug("Pinging Binance Futures Testnet API.")
            res = self.client.futures_ping()
            logger.info("Successfully connected to Binance Futures Testnet.")
            return True
        except BinanceAPIException as e:
            logger.error(f"Binance API Exception during ping: {e}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Exception during ping: {e}")
            raise
        except Exception as e:
            logger.error(f"Network or unknown error during ping: {e}")
            raise

    def get_client(self):
        return self.client
