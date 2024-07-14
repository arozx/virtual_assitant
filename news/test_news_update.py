import os

import dotenv

from news import NewsUpdate

# from news_update import NewsUpdate

dotenv.load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def test_fetch_news():
    # Test case 1: Valid query with default parameters
    news = NewsUpdate(api_key=NEWS_API_KEY)
    result = news.fetch_news(query="technology")
    assert result is not None
    assert "articles" in result

    # Test case 2: Valid query with custom parameters
    result = news.fetch_news(query="sports")
    assert result is not None
    assert "articles" in result


def test_parse_news():
    # Test case 1: Valid news data
    news_data = {
        "articles": [
            {
                "publishedAt": "2021-07-13T12:00:00Z",
                "title": "Sample title",
                "content": "Sample content",
            }
        ]
    }

    news = NewsUpdate(api_key="TEST_API_KEY")
    assert news.parse_news(news_data=news_data) != []

    # Test case 2: Invalid news data
    news_data = {}
    assert news.parse_news(news_data=news_data) == []


test_fetch_news()
