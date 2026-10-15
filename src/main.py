from langgraph.graph import StateGraph, START, END
from state import LinkedInState
from nodes.critic import critic_node
from nodes.writer import writer_node
from nodes.router import route_after_critic

builder = StateGraph(LinkedInState)

builder.add_node("writer",writer_node)
builder.add_node("critic",critic_node)

builder.add_edge(START, "writer")
builder.add_edge("writer","critic")

builder.add_conditional_edges(
    "critic",route_after_critic,
    {
        "rewrite":"writer",
        "end":END
    }
)


graph=builder.compile()

result = graph.invoke({
    "topic": "The rise of AI agents",
    "research": """
AI agents are moving beyond simple chatbots.
They can reason over tasks, use tools,
interact with APIs and execute multi-step workflows.
""",
    "draft": "",
    "critique": "",
    "final_post": "",
    "count":0,
    "score":0
})

print("\n\nDRAFT:\n")
print(result["draft"])

print("\n\nCRITIQUE:\n")
print(result["critique"])


# print(graph.get_graph().draw_mermaid())