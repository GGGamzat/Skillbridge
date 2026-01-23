import aiohttp
import asyncio
import logging
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger(__name__)


class DeribitClient:
    def __init__(self, use_testnet: bool = False):
        self.base_url = "https://test.deribit.com/api/v2/public/" if use_testnet else "https://www.deribit.com/api/v2/public/"

    async def _make_request(self, endpoint: str, params: dict) -> dict:
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}{endpoint}"
                async with session.get(url, params=params, timeout=10) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.warning(f"Request failed: {response.status}")
                        return {}
        except Exception as e:
            logger.warning(f"Request error: {e}")
            return {}

    async def get_ticker_price(self, ticker: str) -> Dict[str, Any]:
        instrument = f"{ticker.upper()}-PERPETUAL"
        data = await self._make_request("ticker", {"instrument_name": instrument})

        if data.get("result"):
            result = data["result"]
            price = result.get("last_price") or result.get("mark_price")
            if price:
                return {
                    "ticker": f"{ticker.upper()}_USD",
                    "price": float(price),
                    "timestamp": int(datetime.now().timestamp())
                }
        return None

    async def get_index_price(self, ticker: str) -> Dict[str, Any]:
        data = await self._make_request("get_index_price", {"index_name": f"{ticker.lower()}_usd"})

        if data.get("result"):
            result = data["result"]
            return {
                "ticker": f"{ticker.upper()}_USD",
                "price": float(result["index_price"]),
                "timestamp": int(result["timestamp"] / 1000)
            }
        return None

    def _get_mock_price(self, ticker: str) -> Dict[str, Any]:
        from random import uniform
        base_prices = {"BTC": 45000.0, "ETH": 2500.0}

        return {
            "ticker": f"{ticker.upper()}_USD",
            "price": base_prices.get(ticker.upper(), 1000.0) * uniform(0.98, 1.02),
            "timestamp": int(datetime.now().timestamp())
        }

    async def get_price(self, ticker: str) -> Dict[str, Any]:
        price = await self.get_ticker_price(ticker)
        if price:
            logger.info(f"Got {ticker} price: ${price['price']:.2f}")
            return price

        price = await self.get_index_price(ticker)
        if price:
            logger.info(f"Got {ticker} index price: ${price['price']:.2f}")
            return price

        logger.info(f"Using mock data for {ticker}")
        return self._get_mock_price(ticker)

    async def get_all_prices(self) -> list:
        btc_price = await self.get_price("btc")
        eth_price = await self.get_price("eth")
        return [btc_price, eth_price]