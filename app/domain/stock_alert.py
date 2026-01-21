from app.constants import STOCK_SYMBOL, COMPANY_NAME, PRICE_CHANGE_THRESHOLD, NEW_ARTICLE_LIMIT

class StockAlert:
    def __init__(self, stock_service, news_service, notifier):
        self.stock_service = stock_service
        self.news_service = news_service
        self.notifier = notifier

    def run(self) -> None:
        prices = self.stock_service.get_daily_close_prices(STOCK_SYMBOL)
        change = self.stock_service.calculate_percentage_change(prices)
        
        if abs(change) < PRICE_CHANGE_THRESHOLD:
            return
        
        articles = self.news_service.get_top_articles(COMPANY_NAME, NEW_ARTICLE_LIMIT)
        message = self._build_message(change, articles)

        self.notifier.send_alert(message)

    def _build_message(self, change: float, articles: list[dict]) -> str:
        direction = "🔺" if change > 0 else "🔻"

        lines = [
            f"{STOCK_SYMBOL}: {direction} {abs(change):.2f}%",
            "",
            "Top news:",
        ]

        for article in articles:
            lines.append(f"- {article['title']}")
            lines.append(f"  {article['description']}")

        return "\n".join(lines)
