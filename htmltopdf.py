import pdfkit

# URL of the webpage you want to convert
url = "https://www.google.com"

# Output PDF file
output_pdf = "output.pdf"

# Configuration for pdfkit with path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

try:
    # Convert webpage to PDF
    pdfkit.from_url(url, output_pdf, configuration=config)
    print(f"The webpage has been successfully converted to {output_pdf}")
except Exception as e:
    print(f"An error occurred: {e}")
