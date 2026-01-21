import requests
from app import config
from app.constants import STOCK_API_BASE_URL

class StockService:
    def get_daily_close_prices(self, symbol: str) -> list[float]:
        """
        Fetch daily close prices from stock API
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": config.STOCK_API_KEY
        }

        response = requests.get(STOCK_API_BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        time_series = data.get("Time Series (Daily)")
        if not time_series:
            raise ValueError("No time series data found")

        # Get the two most recent trading days
        dates = sorted(time_series.keys(), reverse=True)
        if(len(dates) < 2):
            raise ValueError("Not enough data to calculate percentage change")
        latest = float(time_series[dates[0]]["4. close"])
        previous = float(time_series[dates[1]]["4. close"])

        return [latest, previous]

    def calculate_percentage_change(self, prices: list[float]) -> float:
        """
        Compare yesterday vs day before yesterday close prices
        """
        latest, previous = prices
        return ((latest - previous) / previous) * 100
        