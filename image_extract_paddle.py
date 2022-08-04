from pathlib import Path
from paddleocr import PaddleOCR
import pandas as pd

image_path = Path.cwd().joinpath('data','valorant.jpg')

ocr = PaddleOCR(use_angle_cls=True, lang='en')

result = ocr.ocr('./data/valorant.jpg', cls=True)
txt = [line[1][0] for line in result]
print(txt)

df = pd.DataFrame(txt)
print(df.head())
df.to_csv('paddle_results.csv')