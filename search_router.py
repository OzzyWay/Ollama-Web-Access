import ollama
import json


class SearchRouter:

    def __init__(self, model="llama3.2:3b"):
        self.model = model


    def needs_search(self, query):

        prompt = f"""
You are a web search decision system.

Determine if a web search is required.

Return ONLY valid JSON.

Format:

{{
  "search": true,
  "reason": "short explanation"
}}

Rules:

Search = true ONLY when:
- The answer depends on current information
- The user asks for news or recent events
- The user asks for live data
- The user asks for prices, weather, schedules, or rankings

Search = false for:
- Greetings
- Casual conversation
- Programming help
- Explanations
- General knowledge
- Writing requests

User message:
"{query}"
"""


        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0
            }
        )


        raw = response["message"]["content"].strip()


        try:
            decision = json.loads(raw)
            return bool(decision.get("search", False))

        except json.JSONDecodeError:

            print("Router returned invalid JSON:", raw)

            return False