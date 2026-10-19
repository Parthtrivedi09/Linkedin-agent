from state import LinkedInState
from llm import llm


def writer_node(state: LinkedInState):
    prompt = f"""
You are a LinkedIn content writer.

Write a professional LinkedIn post about:

{state["selected_topic"]}

Research:
{state["research"]}

Previous draft:
{state["draft"]}

Critic feedback:
{state["critique"]}

Requirements:
- Strong opening hook
- Easy to read
- Provide useful insight
- Professional but natural tone
- Avoid unnecessary jargon
- Avoid excessive emojis
- End with an engaging question

If a previous draft exists, improve it according to
the critic's feedback.
"""

    response = llm.invoke(prompt)

    return {
        "draft": response.content,
    }