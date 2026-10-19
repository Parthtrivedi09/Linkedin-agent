
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from state import LinkedInState
from nodes.topic_generator import topic_generator
from nodes.topic_approval import topic_approval_node
from nodes.researcher import researcher_node
from nodes.writer import writer_node
from nodes.critic import critic_node
from nodes.router import route_after_critic

def generate_topics_node(state: LinkedInState):
    topics = topic_generator()

    return {
        "candidate_topics": topics
    }


builder = StateGraph(LinkedInState)

builder.add_node("generate_topics", generate_topics_node)
builder.add_node("topic_approval", topic_approval_node)
builder.add_node("researcher", researcher_node)
builder.add_node("writer", writer_node)
builder.add_node("critic", critic_node)

builder.add_edge(START, "generate_topics")
builder.add_edge("generate_topics", "topic_approval")
builder.add_edge("topic_approval", "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", "critic")

builder.add_conditional_edges(
    "critic",
    route_after_critic,
    {
        "rewrite": "writer",
        "end": END
    }
)

checkpointer = MemorySaver()

graph = builder.compile(checkpointer=checkpointer)

config = {
    "configurable": {
        "thread_id": "linkedin-agent-1"
    }
}

initial_state = {
    "candidate_topics": "",
    "selected_topic": "",
    "research": "",
    "draft": "",
    "critique": "",
    "score": 0,
    "count": 0,
    "final_post": ""
}

result = graph.invoke(initial_state, config)

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

print("\nRESEARCH RESULTS:")
print(result["research"])

print("\nFinal draft RESULTS:")
print(result["draft"])
