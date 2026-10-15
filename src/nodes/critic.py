from state import LinkedInState
from llm import llm
from pydantic import BaseModel, Field


class CriticOutput(BaseModel):
    critique: str = Field(description="Detailed feedback on the LinkedIn post")
    score: float = Field(description="Overall post quality score from 0 to 10")


structured_llm=llm.with_structured_output(CriticOutput)


def critic_node(state:LinkedInState):
    prompt = f"""
You are a LinkedIn post critic.

Analyze this post:

{state["draft"]}

Evaluate it on:

1. Hook
2. Value
3. Clarity
4. Engagement
5. Professionalism
6. Originality

Give a score out of 10.

Then provide specific improvements.
"""
    response=structured_llm.invoke(prompt)
    return {
        "score": response.score,
        "critique": response.critique
    }