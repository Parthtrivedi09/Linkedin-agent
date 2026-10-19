
from state import LinkedInState
from nodes.topic_generator import search_web


def researcher_node(state: LinkedInState):
    topic = state["selected_topic"]

    query = f"Latest developments, facts and insights about {topic}"

    results = search_web(query)

    return {
        "research": str(results)
    }
