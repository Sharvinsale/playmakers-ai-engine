# parser/tax1040_parser.py
import pdfplumber

def extract_data(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Dummy example (replace with actual logic)
    data = {
        "total_income": "$125,000",
        "capital_gains": "$18,500",
        "deductions": "$23,000",
        "net_profit": "$35,000"
    }

    return data

import pdfplumber

# parser/tax1040_parser.py

def extract_data(file_path):
    return {
        "total_income": "$125,000",
        "capital_gains": "$18,500",
        "deductions": "$23,000",
        "net_profit": "$35,000"
    }


