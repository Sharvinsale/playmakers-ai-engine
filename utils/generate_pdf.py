from xhtml2pdf import pisa

def generate_pdf(data_dict, insights_text, output_path="playmakers_report.pdf"):
    html = f"""
    <html>
    <head>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        h1 {{ color: #2e86de; }}
        h2 {{ margin-top: 30px; }}
        ul {{ margin-left: 20px; }}
    </style>
    </head>
    <body>
        <h1>Playmakers Financial Report</h1>
        <h2>📄 Summary</h2>
        <ul>
            <li>Total Income: {data_dict.get('total_income')}</li>
            <li>Capital Gains: {data_dict.get('capital_gains')}</li>
            <li>Deductions: {data_dict.get('deductions')}</li>
            <li>Net Profit: {data_dict.get('net_profit')}</li>
        </ul>

        <h2>💡 AI-Generated Insights</h2>
        <p>{insights_text.replace('\n', '<br>')}</p>
    </body>
    </html>
    """

    with open(output_path, "wb") as file:
        pisa.CreatePDF(html, dest=file)

    print(f"✅ PDF generated: {output_path}")
