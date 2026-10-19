
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from state import LinkedInState
from nodes.topic_generator import topic_generator
from nodes.topic_approval import topic_approval_node
from nodes.researcher import researcher_node


def generate_topics_node(state: LinkedInState):
    topics = topic_generator()

    return {
        "candidate_topics": topics
    }


builder = StateGraph(LinkedInState)

builder.add_node("generate_topics", generate_topics_node)
builder.add_node("topic_approval", topic_approval_node)
builder.add_node("researcher", researcher_node)
builder.add_edge(START, "generate_topics")
builder.add_edge("generate_topics", "topic_approval")
builder.add_edge("topic_approval", "researcher")
builder.add_edge("researcher", END)

checkpointer = MemorySaver()

graph = builder.compile(checkpointer=checkpointer)

config = {
    "configurable": {
        "thread_id": "linkedin-agent-1"
    }
}

result = graph.invoke({}, config)

interrupt_data = result["__interrupt__"][0].value

print("\nCANDIDATE TOPICS:\n")
print(interrupt_data["candidate_topics"])

selected_topic = input(
    "\nEnter the topic you want to approve: "
).strip()

if not selected_topic:
    raise ValueError("Topic selection cannot be empty.")

result = graph.invoke(
    Command(resume=selected_topic),
    config
)

print("\nAPPROVED TOPIC:")
print(result["selected_topic"])

print("\nRESEARCH RESULTS:")
print(result["research"])
