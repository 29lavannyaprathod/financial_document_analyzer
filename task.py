# task.py

from crewai import Task
from agents import financial_analyst


analyze_financial_document = Task(
    description=(
        "You are given a financial document.\n"
        "Analyze the document content carefully and answer the user's query: {query}\n\n"

        "Your analysis should include:\n"
        "1. Summary of the document\n"
        "2. Key financial insights\n"
        "3. Important metrics (revenue, profit, etc. if available)\n"
        "4. Potential risks\n"
        "5. Final conclusion\n\n"

        "Only use the provided document content. Do not make assumptions."
    ),

    expected_output=(
        "A structured financial analysis including:\n"
        "- Summary\n"
        "- Key Insights\n"
        "- Financial Metrics\n"
        "- Risks\n"
        "- Conclusion"
    ),

    agent=financial_analyst,
)