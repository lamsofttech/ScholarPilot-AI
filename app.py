from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def research_agent(state):
    topic = state["topic"]
    country = state["country"]

    prompt = f"""
    Find 5 potential PhD programs for a student interested in {topic}
    in {country}. Include university, department, possible funding,
    deadline estimate, and why it fits.
    """

    result = llm.invoke(prompt).content
    return {"research_results": result}


def matching_agent(state):
    prompt = f"""
    Based on these PhD programs, identify likely professor profiles
    and score fit from 1-10.

    Programs:
    {state["research_results"]}

    Student profile:
    {state["profile"]}
    """

    result = llm.invoke(prompt).content
    return {"matches": result}


def outreach_agent(state):
    prompt = f"""
    Write personalized PhD outreach email drafts based on:

    Matches:
    {state["matches"]}

    Student profile:
    {state["profile"]}
    """

    result = llm.invoke(prompt).content
    return {"emails": result}


def document_agent(state):
    prompt = f"""
    Create a Statement of Purpose outline for this PhD applicant.

    Topic:
    {state["topic"]}

    Profile:
    {state["profile"]}

    Matches:
    {state["matches"]}
    """

    result = llm.invoke(prompt).content
    return {"sop_outline": result}


def deadline_agent(state):
    prompt = f"""
    Create an application tracking checklist with deadlines,
    required documents, professor outreach status, and next actions.

    Research:
    {state["research_results"]}

    Matches:
    {state["matches"]}
    """

    result = llm.invoke(prompt).content
    return {"deadline_plan": result}


def decision_agent(state):
    prompt = f"""
    Summarize the best PhD application strategy using all outputs:

    Research:
    {state["research_results"]}

    Matches:
    {state["matches"]}

    Emails:
    {state["emails"]}

    SOP:
    {state["sop_outline"]}

    Deadlines:
    {state["deadline_plan"]}
    """

    result = llm.invoke(prompt).content
    return {"final_plan": result}