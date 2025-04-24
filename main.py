from parser.tax1040_parser import extract_data
from gpt_engine.generate_insights import get_insights
import os

# === Step 1: Load and extract data from PDF ===
file_path = "sample_filled_1040.pdf"

print("📄 Reading PDF and extracting data...")
data = extract_data(file_path)

print("\n🧾 Extracted Data:")
for key, value in data.items():
    print(f"{key}: {value}")

# === Step 2: Generate AI-powered financial summary ===
print("\n💡 Generating AI Insights...")
insights = get_insights(data)

print("\n📈 AI Summary:")
print(insights)

# === Step 3: Save to file ===
output_folder = "reports"
os.makedirs(output_folder, exist_ok=True)
with open(os.path.join(output_folder, "ai_summary.txt"), "w") as f:
    f.write(insights)

print(f"\n✅ Summary saved to {os.path.join(output_folder, 'ai_summary.txt')}")
