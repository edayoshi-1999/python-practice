from PIL import Image
# import matplotlib.pyplot as plt

# im = Image.open(r"chapter12\source\photo5.webp")
# print(im.filename)
# print(im.format)
# print(im.mode)
# print(im.size)
# print(im.width)
# print(im.height)


# size = 300, 200
# color = 0, 164, 233
# print(color)
# im = Image.new("RGB", size, color)
# im.save(r"chapter12\sample.png")
# im.show()
# plt.imshow(im)
# plt.title("Image form PIL")
# plt.show()

# im = Image.open(r"chapter12\source\photo1.jpeg")
# im.save(r"chapter12\target\01元画像.jpg")
# im.convert("L").save(r"chapter12\target\02グレースケール.jpg")
# def multiply(x):
#     return x * 1.5
# im.point(multiply).save(r"chapter12\target\03明るく.jpg")
# r,g,b =im.split()
# r.save(r"chapter12\target\04Redバンド.jpg")
# g.save(r"chapter12\target\04グリーンバンド.jpg")
# b.save(r"chapter12\target\04ブルーバンド.jpg")

# def save_and_print_size(im, stem):
#     im.save(rf"chapter12\target\{stem}.jpg")
#     print(im.size)
# im = Image.open(r"chapter12\source\photo2.jpeg")
# print(im.size) 
# width, height = 1024, 1024 #オリジナルサイズ
# save_and_print_size(im, "01元画像")
# save_and_print_size(im.crop((250, 500, 600, 800)), "02切り取り")
# save_and_print_size(im.resize((width * 2, int(height / 2))), "03リサイズ")
# im.thumbnail((width * 2, height / 2))
# save_and_print_size(im, "04サムネイル")

# def save_and_print_size(im, stem):
#     im.save(rf"chapter12\target\{stem}.jpg")
#     print(im.size)
# im = Image.open(r"chapter12\source\photo3.jpeg")
# width, height = 1024, 1024 #オリジナルサイズ
# save_and_print_size(im, "01元画像")
# save_and_print_size(im.rotate(90), "02回転90度")
# save_and_print_size(im.resize((width * 2, int(height / 2))).rotate(90, expand=True), "03回転90度拡張")
# save_and_print_size(im.rotate(180), "04回転180度")
# save_and_print_size(im.transpose(Image.FLIP_LEFT_RIGHT), "05左右反転")
# save_and_print_size(im.transpose(Image.FLIP_TOP_BOTTOM), "06上下反転")

def save_and_print_size(im, stem):
    im.save(rf"chapter12\target\{stem}.jpg")
    print(im.size)

im = Image.open(r"chapter12\source\photo4.jpeg")

# save_and_print_size(im, "01元画像")

# im_paste = im.copy()
# im_paste.paste(im.crop((300, 300, 500, 500)), (50, 50))
# save_and_print_size(im_paste, "02型貼り付け")

watermark = Image.open(r"chapter12\watermark.png")
im_watermark = im.copy()
# im_watermark.paste(watermark, (500, 500), watermark)
# save_and_print_size(im_watermark, "03透かし貼り付け")
im_watermark.paste(watermark, (0,0))
save_and_print_size(im_watermark, "04透かし貼り付けmaskなし")