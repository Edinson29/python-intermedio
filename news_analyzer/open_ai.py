"""Integration with OpenAI API for advanced text analysis and generation."""

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def analyze_news_with_ai(articles: list[dict], query: str) -> str | None:
    """Use OpenAI API to analyze news articles based on a specific query.
    Args:
        articles (list[dict]): A list of news articles, each containing a 'content' key with the article's text.
        query (str): The analysis query or prompt to send to the OpenAI API.
    Returns:
        str | None: The response from the OpenAI API, or None if an error occurs.
    """
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        context = "\n".join(
            [
                f"- {article['title']}: {article.get('description', '')[:100]} ..."
                for article in articles[:10]
            ]
        )

        prompt = f"""
            Basandote en estás noticias:
            {context}

            Pregunta: {query}

            Response de forma concisa en español.
        """

        print(f"Prompt: {prompt}")

        response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="Eres un agente que lee contexto y responde de manera concisa en español.",
            input=prompt,
        )

        print(response.output_text)
    except Exception as e:
        print(f"Error analyzing news with AI: {e}")
        return None