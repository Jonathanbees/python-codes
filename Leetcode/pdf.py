import PyPDF2
from summarizer import Summarizer

def summarize_pdf(file_path):
    # Open the PDF file in binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Initialize an empty string to hold the text
        text = ''

        # Loop through each page in the PDF and extract the text
        for page_number in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_number)
            text += page.extractText()

    # Use BERT summarizer
    model = Summarizer()
    summary = model(text)

    return summary

# Use the function
print(summarize_pdf('../../Downloads/MariaTeresaUribe-Las soberanías-en-disputa.pdf'))