# import qrcode
# import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image


# im = qrcode.make("https://tonari-it.com")
# plt.imshow(im)
# plt.title("Image form PIL")
# plt.show()

# qr = qrcode.QRCode(
#     error_correction=qrcode.ERROR_CORRECT_H,
#     box_size=5,
#     border=8
# )
# qr.add_data("https://tonari-it.com")
# qr.make()
# im = qr.make_image(back_color="white", fill_color="blue")
# plt.imshow(im)
# plt.title("Image form PIL")
# plt.show()
# print(qr.box_size)
# print(qr.border)
# print(qr.data_list)

# img = Image(r"chapter13/photo.png")
# print(img.format)
# print(img.anchor)
# print(img.ref)
# wb = Workbook()
# ws = wb.active
# ws.add_image(img)
# wb.save(r"chapter13/photo.xlsx")

# px = 100
# height, width = px, px / 100
# wb = Workbook()
# ws = wb.active
# ws.row_dimensions[1].height = height
# ws.column_dimensions["A"].width = width
# wb.save(r"chapter13/dimension.xlsx")