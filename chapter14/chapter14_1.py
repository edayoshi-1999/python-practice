from PyPDF2 import PdfMerger, PdfWriter, PdfReader, Transformation
from PyPDF2.pagerange import PageRange
from PyPDF2 import PageObject

writer = PdfWriter()
reader = PdfReader(r"chapter14\pdf\基礎物理レポート6-27.pdf")

page1 = reader.pages[0]
width = page1.mediabox.width
height = page1.mediabox.height
new_page = PageObject.create_blank_page(width=width*2, height=height)

new_page.merge_page(page1)

page2 = reader.pages[1]

page2.mediabox.lower_left = (0, 0)
page2.mediabox.upper_right = (width*2, height)
page2.add_transformation(Transformation().translate(tx=float(width), ty=0))

new_page.merge_page(page2)

writer.add_page(new_page)

with open(r"chapter14\pdf\page_obj9.pdf", "wb") as f:
    writer.write(f)

# writer = PdfWriter()
# reader = PdfReader(r"chapter14\pdf\基礎物理レポート6-27.pdf")
# page1 = reader.pages[0]
# writer.add_page(page1)
# width = page1.mediabox.width
# height = page1.mediabox.height
# page2 = PageObject.create_blank_page(width=width, height=height)
# writer.add_page(page2)
# with open(r"chapter14\pdf\page_obj.pdf", "wb") as f:
#     writer.write(f)

# source = r"chapter14\pdf\基礎物理レポート6-27.pdf"
# pages = PageRange("::2")
# merger = PdfMerger()
# merger.append(source, pages=pages)
# merger.write(r"chapter14\pdf\write_2.pdf")
# merger.close()

# writer = PdfWriter()
# reader = PdfReader(r"chapter14\pdf\基礎物理レポート6-27.pdf")
# numPages = len(reader.pages)
# for i in range(0, numPages, 2):
#     page = reader.pages[i]
#     writer.add_page(page)
# with open(r"chapter14\pdf\write.pdf", "wb")as f:
#     writer.write(f)

# def split_pdf(source_file, pages, splited_file):
#     merger = PdfMerger()
#     merger.append(source_file, pages=pages)
#     merger.write(splited_file)
#     merger.close()
# source = r"chapter14\pdf\基礎物理レポート6-27.pdf"
# split_pdf(source, PageRange(":2"), r"chapter14\pdf\split_1.pdf")
# split_pdf(source, PageRange("2:"), r"chapter14\pdf\split_2.pdf")

# reader = PdfReader(r"chapter14\pdf\スキャンした書類.pdf")
# chapter14\pdf\スキャンした書類.pdf
# chapter14\pdf\基礎物理レポート6-27.pdf
# print(len(reader.pages))
# print(type(reader.metadata))

# doc_info = reader.metadata
# print(doc_info.title)
# print(doc_info.author)
# for key in doc_info.keys():
#     print(key, ":", doc_info[key])

# merger = PdfMerger()
# merger.append(r"chapter14\pdf\基礎物理レポート6-27.pdf")
# merger.append(r"chapter14\pdf\スキャンした書類.pdf")
# merger.write(r"chapter14\pdf\merge.pdf")
# merger.close()

