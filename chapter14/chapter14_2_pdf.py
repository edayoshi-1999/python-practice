import pandas as pd
from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation

writer = PdfWriter()

df = pd.read_excel(r"chapter14\PDFリスト.xlsx")

for record in df.values:

    reader = PdfReader(record[0])
    numPages = len(reader.pages)
    box = reader.pages[0].mediabox
    width, height = box.width, box.height
    print(record[0], numPages, width, height)

    # ある一個分のpdfファイルについての処理
    for i in range(0, numPages, 2):
        new_page = PageObject.create_blank_page(width=width*2, height=height)
        
        # 左側にページを張る。
        page1 = reader.pages[i]
        new_page.merge_page(page1)

        # ページ数が偶数の場合、最後のページを右側に貼り付ける操作をする
        if i <= len(reader.pages) - 2:
            page2 = reader.pages[i + 1]
            page2.mediabox.lower_left = (0, 0)
            page2.mediabox.upper_right = (width*2, height)
            page2.add_transformation(Transformation().translate(tx=float(width), ty=0))
            new_page.merge_page(page2)

        writer.add_page(new_page)

with open(r"chapter14\2in1.pdf", "wb") as f:
    writer.write(f)