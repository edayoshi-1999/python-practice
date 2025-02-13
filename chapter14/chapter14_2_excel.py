import pathlib
from PyPDF2 import PdfReader
import pandas as pd

my_path = pathlib.Path(r"chapter14\pdf")

values = []
for p in my_path.glob("*.pdf"):
    reader = PdfReader(str(p))
    numPages = len(reader.pages)
    create_date = reader.metadata["/CreationDate"]
    mod_date = reader.metadata["/ModDate"]
    values.append([str(p), create_date, mod_date, numPages])
    
columns = ["ファイル名", "作成日時", "更新日時", "ページ番号"]
df = pd.DataFrame(values, columns=columns)
df.to_excel(r"chapter14\PDFリスト.xlsx", index=False)

