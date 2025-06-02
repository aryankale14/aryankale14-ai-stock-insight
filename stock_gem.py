
from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.tools.googlesearch import GoogleSearch

agent = Agent(
    model=Gemini(id="gemini-2.5-flash-preview-05-20"),
    tools=[GoogleSearch()],
    description="You are a finance bot that provides the latest news and latest stock data.",
    instructions=[
        "Given a stock provided by the user, use the GoogleSearch tool to retrieve the latest stock price with date and provide 4 recent news items about the company.",
        "Use the GoogleSearch tool to find latest sources that tell expert opinions and analyst ratings (e.g., Buy, Sell, or Hold recommendations).",
        "Use the GoogleSearch tool to identify latest sources that predict the future price and categorize them into bullish, neutral, and bearish predictions.",
        "Use the GoogleSearch tool to find recent news articles.",
        "Search in English.",
    ],
)

def run_stock_analysis(stock_name: str) -> str:
    response: RunResponse = agent.run(stock_name)
    return response.content
