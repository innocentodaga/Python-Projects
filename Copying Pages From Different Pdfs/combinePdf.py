# This is what our program will do

# • Find all PDF files in the current working directory.
# • Sort the filenames so the PDFs are added in order.
# • Write each page, excluding the first page, of each PDF to the 
# output file

import PyPDF2, os

# Get all te pdf filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfWriter = PyPDF2.PdfWriter()

# Loop thru all the pdf files.
for filename in pdfFiles:
    pdfFileObject = open(filename, 'rb')
    pdfReader =  PyPDF2.PdfReader(pdfFileObject)
    
    # Loop thru all the pages except the first and add them
    for pageNum in range(1, len(pdfReader.pages)):
        pageObject  = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObject)

# save the resulting PDF to a file
pdfOutPut  = open("allminutes.pdf", 'wb')
pdfWriter.write(pdfOutPut)
pdfOutPut.close()
