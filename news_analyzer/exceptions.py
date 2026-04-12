class NewsSystemError(Exception):
    """Base class for news system errors."""
    pass

class APIKeyError(NewsSystemError):
    """Raised when the API key is missing or invalid."""
    pass