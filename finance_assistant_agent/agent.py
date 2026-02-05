from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from typing import Dict

def get_user_personal_finance_details() -> Dict:
    """
        Gets users personal finance details like salary, expense and savings capacity
    """
    return{
        "salary":50000,
        "expense":40000,
        "savings":10000
    }

finance_assistant_agent = LlmAgent(
    name="finance_assistant_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistant that helps with user's finance goals.",
    instruction="""You are a friendly finance assistant.
                    You can help answer user's generic questions on finance and help plan 
                    their finance goals. Be more friendly and positive.
                    """,
    tools=[get_user_personal_finance_details, google_search]
)

root_agent = finance_assistant_agent