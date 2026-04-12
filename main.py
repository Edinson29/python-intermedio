

from news_analyzer.exceptions import APIKeyError
from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.utils import get_unique_sources, get_articles_by_sources, get_reading_time

from dotenv import load_dotenv
load_dotenv()  # Carga las variables del archivo .env


response_data = None
try:
    response_data = fetch_news("newsapi", API_KEY, "python")
except APIKeyError as e:
    print(f"API Key error: {e}")

if response_data:
    sources_set: set = get_unique_sources(response_data.get("articles", []))
    for index, source in enumerate(sources_set, start=1):
        print(f"No: {index} -- { source}")

    articles: list[dict] = list(map(get_reading_time, response_data["articles"]))
    for article in articles:
        print(f"""{article["title"]} -- Reading time: {article["reading_time"]} minute(s)""")

    xataka_articles: list[dict] = get_articles_by_sources(response_data.get("articles"), "github.io")
    for xataka_article in xataka_articles:
        print(f"""{xataka_article["source"]["name"]} - {xataka_article["title"]}""")