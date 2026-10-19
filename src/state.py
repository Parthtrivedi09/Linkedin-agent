from typing import TypedDict

class LinkedInState(TypedDict):
    candidate_topics: str
    selected_topic: str
    research: str
    draft: str
    critique: str
    score: int
    count: int
    final_post: str