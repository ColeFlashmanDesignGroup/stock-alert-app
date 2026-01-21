import requests
from app.config import NEWS_API_KEY
from app.constants import NEWS_API_BASE_URL

class NewsService:
    def get_top_articles(self, company_name: str, limit: int = 3) -> list[dict]:
        """
        Fetch top N news articles from news API
        """
        params = {
            "q": company_name,
            "sortBy": "publishedAt",
            "language": "en",
            "apiKey": NEWS_API_KEY,
        }

        response = requests.get(NEWS_API_BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        articles = data.get("articles", [])

        return [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
            }
            for article in articles[:limit]
        ]