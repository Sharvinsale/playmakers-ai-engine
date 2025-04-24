import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_insights(data):
    prompt = f"""
Here is a client's financial summary extracted from IRS Form 1040:

- First Name: {data['first_name']}
- Last Name: {data['last_name']}
- Total Income: ${data['total_income']}
- Capital Gains: ${data['capital_gains']}
- Deductions: ${data['deductions']}
- Adjusted Gross Income (AGI): ${data['agi']}
- Taxable Income: ${data['taxable_income']}

Please generate a clear, professional summary that includes:
1. A brief overview of the client's financial position
2. 2–3 personalized tax-saving or advisory strategies
3. A financial health flag if any value stands out

Make the output sound like it's written by a financial advisor.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
