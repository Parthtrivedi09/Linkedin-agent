from state import LinkedInState

def route_after_critic(state: LinkedInState):

    if state["score"] >= 8:
        print("ROUTING TO END")
        return "end"

    print("ROUTING TO WRITER")
    return "rewrite"