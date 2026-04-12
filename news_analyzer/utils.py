"""Utilities for the news analyzer package."""


def get_unique_sources(articles: list[dict]) -> set:
    """Extract unique news sources from a list of articles.
    Args:
        articles (list[dict]): A list of news articles, each containing a 'source' key.
    Returns:
        set: A set of unique news source names.
    """
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")    
    }