from PyPDF2 import PdfReader

def clean_currency(value):
    try:
        return float(value.replace(",", "").strip())
    except:
        return None

def extract_data(file_path):
    reader = PdfReader(file_path)
    fields = reader.get_fields()

    return {
        "first_name": fields.get("f1_04[0]", {}).get("/V", "Not found"),
        "last_name": fields.get("f1_05[0]", {}).get("/V", "Not found"),
        "ssn": fields.get("f1_06[0]", {}).get("/V", "Not found"),
        "total_income": clean_currency(fields.get("f1_54[0]", {}).get("/V", "0")),
        "capital_gains": clean_currency(fields.get("f1_52[0]", {}).get("/V", "0")),
        "deductions": clean_currency(fields.get("f1_57[0]", {}).get("/V", "0")),
        "agi": clean_currency(fields.get("f1_56[0]", {}).get("/V", "0")),
        "taxable_income": clean_currency(fields.get("f1_60[0]", {}).get("/V", "0"))
    }
