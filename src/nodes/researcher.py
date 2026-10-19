from langchain_community.tools import DuckDuckGoSearchResults
from state import LinkedInState

search_tool = DuckDuckGoSearchResults(
    output_format="list",
    num_results=5
)


def researcher_node(state: LinkedInState):
    query = f"Latest developments and insights about {state['topic']}"

    results = search_tool.invoke(query)

    return {
        "research": str(results)
    }