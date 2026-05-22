from app.config import client, OPENAI_MODEL


def generate_dashboard_plan(df, roles):

    sample = df.sample(min(30, len(df))).to_string()

    prompt = f"""
You must return JSON with EXACT structure:

{{
  "dashboard_title": "string",
  "charts": [
    {{
      "chart_type": "bar|line|pie",
      "x": "column",
      "y": "column",
      "aggregation": "sum|avg|count",
      "title": "string"
    }}
  ]
}}

Rules:
- MUST include "charts" array
- MUST include at least 2 charts
- NO missing fields

DATA:
{sample}

COLUMN ROLES:
{roles}

Return ONLY valid JSON.
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are a BI assistant. You must respond ONLY with JSON."
            },
            {
                "role": "user",
                "content": "Return a JSON dashboard plan. " + prompt
            }
        ]
    )

    return response.choices[0].message.content