
import requests
from llm import llm


def search_web(query):
    response = requests.get(
        "https://freeserp.ai/api.php",
        params={
            "index": "web",
            "q": query,
            "size": 5
        },
        timeout=30
    )

    response.raise_for_status()
    return response.json()


def topic_generator():
    queries = [
        "latest generative AI developments",
        "latest AI agents and LLM developments"
    ]

    search_results = []

    for query in queries:
        results = search_web(query)
        search_results.append(results)

    prompt = f"""
You are a LinkedIn content strategist specializing in AI.

Based on the following web search results, suggest five
promising LinkedIn post topics.

Search results:
{search_results}

Requirements:
- Focus on Generative AI, Agentic AI, LLMs and AI engineering.
- Prefer recent developments and useful technical insights.
- Avoid duplicate topics.
- Explain why each topic is worth posting about.
- Do not invent facts unsupported by the results.

Return five numbered topics with short explanations.
"""

    response = llm.invoke(prompt)
    return response.content
