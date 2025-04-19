from dotenv import load_dotenv
import os
from parser.tax1040_parser import extract_data
from gpt_engine.generate_insights import get_insights

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ OPENAI_API_KEY not loaded. Check your .env file format.")
    print("Current Working Directory:", os.getcwd())
    exit()

print("✅ OpenAI key loaded:", api_key[:10], "...")




file_path = "sample_1040.pdf"

# Extract values
data = extract_data(file_path)
print("📄 Extracted Data:", data)

# Send to GPT
insights = get_insights(data)
print("\n💡 AI Insights:\n", insights)

from dotenv import load_dotenv
import os

from parser.tax1040_parser import extract_data
from gpt_engine.generate_insights import get_insights

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY not loaded.")
    exit()

print("✅ OpenAI key loaded:", api_key[:10], "...")

# === Step 1: Load PDF and extract data ===
file_path = "sample_1040.pdf"
data = extract_data(file_path)
print("\n📄 Extracted Data:\n", data)

# === Step 2: Generate insights from GPT ===
insights = get_insights(data)
print("\n💡 AI Insights:\n", insights)

