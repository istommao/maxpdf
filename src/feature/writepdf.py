from pathlib import Path


def write_pdf(pdf_merger, save_path):
    with Path(save_path).open(mode="wb") as output_file:
        pdf_merger.write(output_file)

    return pdf_merger
