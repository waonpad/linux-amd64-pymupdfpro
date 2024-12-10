import pymupdf.pro

pymupdf.pro.unlock()

test_docx = "test.docx"
test_pptx = "test.pptx"
test_xlsx = "test.xlsx"


def main():
    print("==== Testing docx ====")
    docx = pymupdf.open(test_docx)
    docx_page = docx.load_page(0)
    print(docx_page.get_textpage().extractHTML())

    print("==== Testing pptx ====")
    pptx = pymupdf.open(test_pptx)
    pptx_page = pptx.load_page(0)
    print(pptx_page.get_textpage().extractHTML())

    print("==== Testing xlsx ====")
    xlsx = pymupdf.open(test_xlsx)
    xlsx_page = xlsx.load_page(0)
    print(xlsx_page.get_textpage().extractHTML())


if __name__ == "__main__":
    main()
