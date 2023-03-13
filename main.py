from PyPDF2 import PdfReader, PdfWriter
with open("documents/cuffGuide.pdf", "rb") as in_file:
    input_pdf = PdfReader(in_file)

    output_pdf = PdfWriter()
    output_pdf.append_pages_from_reader(input_pdf)
    output_pdf.encrypt("password")

    with open("output.pdf", "wb") as out_file:
        output_pdf.write(out_file)
