from PIL import Image
from pathlib import Path

import pytesseract as pt

image_path = Path.cwd().joinpath('data','valorant.jpg')
img = Image.open(image_path)
new_size = tuple(2*x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
print(pt.image_to_string(img))

pdf = pt.image_to_pdf_or_hocr(img, extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

