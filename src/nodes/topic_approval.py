from langgraph.types import interrupt
from state import LinkedInState

def topic_approval_node(state:LinkedInState):
    selected_topic = interrupt({
        "message":"choose a topic for the post",
        "candidate_topics":state["candidate_topics"]
    })
    return {
        "selected_topic":selected_topic
    }