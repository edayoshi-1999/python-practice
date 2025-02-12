import pathlib
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import qrcode

fp_xlsx = r"chapter13\記事一覧3.xlsx"
wb = load_workbook(fp_xlsx)
ws = wb.active

print(10)

fp = pathlib.Path(r"chapter13\qr.png")
size = (100, 100)
height, width = 75, 14.5

for i, record in enumerate(ws.values):
    if i == 0: continue #1行目はヘッダーなので飛ばす

    url = record[2]
    im = qrcode.make(url).resize(size)
    im.save(fp)

    img = Image(fp)
    row = i + 1
    ws.add_image(img, f"D{row}")
    ws.row_dimensions[row].height = height

ws.column_dimensions["D"].width = width
wb.save(fp_xlsx)
fp.unlink()