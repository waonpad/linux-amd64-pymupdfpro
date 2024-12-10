import os

import pymupdf.pro

test_docx = "test.docx"
test_pptx = "test.pptx"
test_xlsx = "test.xlsx"


def main():
    cwd = os.getcwd()

    # Print added font paths
    os.environ["PYMUPDFPRO_FONT_PATH_VERBOSE"] = "1"

    pymupdf.pro.unlock(
        # Font files are located in the `fonts` directory
        # e.g. /path/to/fonts/SomeFont.ttf
        fontpath=f"{cwd}/fonts",
        # Disable automatic font path detection
        fontpath_auto=False,
    )

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
