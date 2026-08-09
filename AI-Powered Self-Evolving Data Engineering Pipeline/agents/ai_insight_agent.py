import json
from ollama import chat


class AIInsightAgent:

    def generate_ai_insights(
        self,
        total_revenue,
        top_product,
        top_customer
    ):

        with open(
            "memory/rules.json",
            "r",
            encoding="utf-8"
        ) as f:

            rules = json.load(f)

        prompt = f"""
You are a Retail Business Analyst.

Current Business Rules:

Sales Drop Threshold:
{rules['sales_drop_threshold']}%

Seasonality Check Enabled:
{rules['seasonality_check']}

Quality Threshold:
{rules['quality_threshold']}%

Analyze ONLY the information provided.

Do NOT invent trends,
percentages,
historical comparisons,
or customer behavior not present in the data.

If information is missing,
state:
"Insufficient data available."

Data:

Total Revenue: {total_revenue}
Top Product: {top_product}
Top Customer: {top_customer}

Generate:

1. Key Insights
2. Risks
3. Recommendations

If seasonality_check is enabled,
consider seasonal business patterns
before generating warnings.

Keep the response concise.
"""
        print("\n========== PROMPT SENT TO OLLAMA ==========\n")
        print(prompt)

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