from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents import (
    research_agent,
    matching_agent,
    outreach_agent,
    document_agent,
    deadline_agent,
    decision_agent,
)

class PhDState(TypedDict):
    topic: str
    country: str
    profile: str
    research_results: str
    matches: str
    emails: str
    sop_outline: str
    deadline_plan: str
    final_plan: str


def build_graph():
    graph = StateGraph(PhDState)

    graph.add_node("research", research_agent)
    graph.add_node("matching", matching_agent)
    graph.add_node("outreach", outreach_agent)
    graph.add_node("documents", document_agent)
    graph.add_node("deadlines", deadline_agent)
    graph.add_node("decision", decision_agent)

    graph.set_entry_point("research")
    graph.add_edge("research", "matching")
    graph.add_edge("matching", "outreach")
    graph.add_edge("outreach", "documents")
    graph.add_edge("documents", "deadlines")
    graph.add_edge("deadlines", "decision")
    graph.add_edge("decision", END)

    return graph.compile()