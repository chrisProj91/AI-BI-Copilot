from app.config import client, OPENAI_MODEL

def ask_data_question(df, question):

    sample = df.head(30).to_string()

    prompt = f"""
You are a data analyst.

DATA:
{sample}

QUESTION:
{question}

Answer clearly using only given data.
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content