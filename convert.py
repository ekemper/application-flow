import pdfkit

output_file = "Edward Kemper resume - OpenLoop TPM.pdf"

def html_to_pdf(input_html, output_file):
    pdfkit.from_file(input_html, output_file)

if __name__ == "__main__":
        
    input_file = "resume-proto-OpenLoop-TPM.html"
    

    # Optional config if wkhtmltopdf isn't in your PATH:
    # config = pdfkit.configuration(wkhtmltopdf='/opt/homebrew/bin/wkhtmltopdf')
    # pdfkit.from_file(input_file, output_file, configuration=config)

    pdfkit.from_file(input_file, output_file)

    print(f"PDF saved to {output_file}")
