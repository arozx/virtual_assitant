import requests


class NewsUpdate:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def fetch_news(
        self,
        query: str,
        from_date: str = None,
        to_date: str = None,
        language: str = "en",
    ):
        params = {
            "q": query,
            "apiKey": self.api_key,
            "from": from_date,
            "to": to_date,
            "language": language,
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch news (status code: {response.status_code})")
            return None

    def parse_news(self, news_data):
        if not news_data or "articles" not in news_data:
            print("Error: No articles found in the news data")
            return []

        parsed_articles = []
        for article in news_data["articles"]:
            # convert date to day-month-year format in words
            parsed_article = {
                "publishedAt": article.get("publishedAt").split("T")[0],
                "title": article.get("title"),
                "content": article.get("content"),
            }
            parsed_articles.append(parsed_article)

        return parsed_articles
