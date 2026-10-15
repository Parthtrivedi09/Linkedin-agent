from typing import TypedDict

class LinkedInState(TypedDict):
    topic:str
    research:str
    draft:str
    critique:str
    score: float
    count:int
    final_post: str
