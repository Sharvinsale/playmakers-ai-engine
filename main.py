from dotenv import load_dotenv
import os

# Your custom modules
from parser.tax1040_parser import extract_data
from gpt_engine.generate_insights import get_insights
from utils.generate_pdf import generate_pdf

# ✅ Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    print("❌ OpenAI API key not found in .env!")
    exit()

print(f"✅ OpenAI key loaded: {openai_key[:10]}...")

# 📄 Path to your test PDF
file_path = "sample_1040.pdf"

# ✅ Step 1: Extract financial data from PDF
extracted_data = extract_data(file_path)
print("📄 Extracted Data:", extracted_data)

# ✅ Step 2: Send extracted data to GPT for insights
insights = get_insights(extracted_data)
print("\n💡 AI Insights:\n", insights)

# ✅ Step 3: Generate a PDF report from extracted + AI data
generate_pdf(extracted_data, insights)

print("🎯 Done! Your client-ready report is ready as 'playmakers_report.pdf'")
