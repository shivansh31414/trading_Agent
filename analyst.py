from crewai import Agent, LLM
from tools.stock_research_Tool import get_stock_price
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("api_key")
)

analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=(
        "Perform in-depth market analyses and deep dives into publicly traded stocks using real-time data. "
        "Try to identify performance insights and key financial signals to support decision-making."
    ),
    backstory=(
        "You are a veteran financial analyst with deep expertise in interpreting stock market data, "
        "technical trends, and fundamentals. You specialize in producing well-structured reports that evaluate "
        "stock performance using live market indicators."
    ),
    llm=llm,
    tools=[get_stock_price],
    verbose=True
)


