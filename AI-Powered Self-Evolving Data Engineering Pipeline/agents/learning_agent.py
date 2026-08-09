import json
from ollama import chat


class LearningAgent:

    def learn_from_feedback(self, feedback_records):

        prompt = f"""
You are an AI Learning Agent.

Analyze the following feedback records:

{feedback_records}

Provide:

1. Root causes of incorrect insights.
2. Suggested business rule changes.
3. Expected improvements.

Keep response concise.
"""

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content

    def update_rules(self):

        with open(
            "memory/rules.json",
            "r",
            encoding="utf-8"
        ) as f:

            rules = json.load(f)

        rules["seasonality_check"] = True

        with open(
            "memory/rules.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                rules,
                f,
                indent=4
            )

        return rules