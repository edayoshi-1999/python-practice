import pathlib
from PIL import Image

width_w, height_w = 250, 130
width_im, height_im = 300, 200
x, y = int((width_im - width_w) / 2), int((height_im - height_w) / 2)

watermark = Image.open(r"chapter12\watermark.png").resize((width_w, height_w))
source = r"chapter12\source"
target = r"chapter12\target"

for p in pathlib.Path(source).glob("*.jpeg"):
    print(p)
    im = Image.open(p).resize((width_im, height_im))
    im.paste(watermark, (x,y), watermark)
    im.save(fr"{target}\{p.stem}.jpeg")