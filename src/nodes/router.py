from state import LinkedInState

def route_after_critic(state: LinkedInState):
    print(f"Score: {state['score']}, Count: {state['count']}")

    if state["score"] >= 9 or state["count"] >= 3:
        print("ROUTING TO END")
        return "end"

    print("ROUTING TO WRITER")
    return "rewrite"