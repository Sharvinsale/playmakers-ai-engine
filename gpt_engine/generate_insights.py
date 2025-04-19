import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_insights(data):
    prompt = f"""
    Here's a client's financial data:
    - Total Income: {data['total_income']}
    - Capital Gains: {data['capital_gains']}
    - Deductions: {data['deductions']}
    - Net Profit: {data['net_profit']}

    Please provide:
    1. Two tax-saving strategies
    2. Two financial red flags
    3. One personalized recommendation for their financial advisor
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a financial analyst helping CPAs and wealth managers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_insights(data):
    prompt = f"""
    Here's a client's financial data:
    - Total Income: {data['total_income']}
    - Capital Gains: {data['capital_gains']}
    - Deductions: {data['deductions']}
    - Net Profit: {data['net_profit']}

    Please provide:
    1. Two tax-saving strategies
    2. Two financial red flags
    3. One personalized recommendation for their financial advisor
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a financial analyst helping CPAs and wealth managers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
