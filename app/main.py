from fastapi import FastAPI

from app.services.stock_service import StockService
from app.services.news_service import NewsService
from app.services.notification_service import NotificationService
from app.domain.stock_alert import StockAlert
from app.constants import STOCK_SYMBOL, COMPANY_NAME

from fastapi import HTTPException

app = FastAPI(title="Stock Alert API")

stock_service = StockService()
news_service = NewsService()
notification_service = NotificationService()

alert_service = StockAlert(
    stock_service=stock_service,
    news_service=news_service,
    notifier=notification_service,
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/stock/change")
def get_stock_change():
    try:
        prices = stock_service.get_daily_close_prices(STOCK_SYMBOL)
        change = stock_service.calculate_percentage_change(prices)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    return {
        "symbol": STOCK_SYMBOL,
        "latest_close": prices[0],
        "previous_close": prices[1],
        "percentage_change": round(change, 2),
    }

@app.get("/news")
def get_news():
    articles = news_service.get_top_articles(COMPANY_NAME)

    return {
        "company": COMPANY_NAME,
        "articles": articles,
    }

@app.post("/alert/run")
def run_alert():
    alert_service.run()
    return {"message": "Alert process executed"}
