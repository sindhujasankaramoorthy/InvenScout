import json
from app.clients.llm_client import LLMClient


class QueryService:

    def __init__(self):
        self.llm = LLMClient()

    def expand_query(self, idea):

        prompt = f"""
You are a patent search assistant helping expand a plain-English invention
description into multiple search-ready queries.

Given the user's idea, generate:

1. TWO consumer-style queries
2. THREE technical/patent-style queries
3. TWO adjacent-concept queries

Rules:
- Technical queries must use formal engineering terminology.
- Avoid brand names.
- Do not copy the user's exact wording in technical queries.
- Keep every query under 10 words.
- Output ONLY valid JSON.
- Do not include markdown fences or explanations.

Output format:
{{
  "consumer_queries": ["...", "..."],
  "technical_queries": ["...", "...", "..."],
  "adjacent_queries": ["...", "..."]
}}

User's idea:
{idea}
"""

        result = self.llm.generate(prompt)

        return json.loads(result)