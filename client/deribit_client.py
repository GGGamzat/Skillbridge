import aiohttp
import asyncio
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class DeribitClient:
    def __init__(self, base_url: str = "https://www.deribit.com/api/v2/public/"):
        self.base_url = base_url

    async def get_index_price(self, ticker: str) -> Dict[str, Any]:
        async with aiohttp.ClientSession() as session:
            try:
                index_name = f"{ticker.upper()}_usd" if "_" not in ticker else ticker.upper()
                url = f"{self.base_url}get_index_price"
                params = {"index_name": index_name}

                async with session.get(url, params=params) as response:
                    data = await response.json()

                    if "result" in data:
                        return {
                            "ticker": ticker.upper(),
                            "price": data["result"]["index_price"],
                            "timestamp": int(data["result"]["timestamp"] / 1000)
                        }
                    else:
                        logger.error(f"Error fetching price for {ticker}: {data}")
                        return None

            except Exception as e:
                logger.error(f"Exception in get_index_price for {ticker}: {e}")
                return None

    async def get_prices(self, tickers: list = None) -> list:
        if tickers is None:
            tickers = ["btc_usd", "eth_usd"]

        tasks = []
        for ticker in tickers:
            ticker_clean = ticker.replace("_", "").lower()
            tasks.append(self.get_index_price(ticker_clean))

        results = await asyncio.gather(*tasks)
        return [result for result in results if result is not None]