"""merge pdf"""
from PyPDF2 import PdfFileMerger


def merge_pdf(pdf_list):
    pdf_merger = PdfFileMerger()
    for pdf_path in pdf_list:
        # only the specified range of pages from the source
        # document into the output document

        pages = (0, 1)
        pdf_merger.append(pdf_path, pages=pages, import_bookmarks=False)

    return pdf_merger
