from src.config import PROJECT_RESOURCES_DIR
from src.feature.mergepdf import merge_pdf
from src.feature.writepdf import write_pdf


def test_merge_pdf():
    pdf_list = [
        PROJECT_RESOURCES_DIR + '/owasp_scp_quick_reference_guide.pdf',
        PROJECT_RESOURCES_DIR + '/bash_cheat_sheet.pdf',
    ]
    merger = merge_pdf(pdf_list)
    write_pdf(merger, PROJECT_RESOURCES_DIR + '/mergetest.pdf')
