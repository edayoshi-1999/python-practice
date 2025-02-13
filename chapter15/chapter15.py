import shutil
from pathlib import Path

# shutil.copy2(r"chapter15\data\CCCC.txt", r"chapter15")
# shutil.copy2(Path(r"chapter15\data\DDDD.txt"), Path(r"chapter15"))
# shutil.copytree(r"chapter15\data", r"chapter15\data2")

# shutil.move(r"chapter15\data\AAAA.xlsx", r"chapter15")
# shutil.move(r"chapter15\data\BBBB.xlsx", r"chapter15\data\ZZZZ.xlsx")
# shutil.move(r"chapter15\data2", r"chapter15\data")

# shutil.make_archive(r"chapter15\data\data2", "zip", r"chapter15\data")
# shutil.unpack_archive(Path(r"chapter15\data2.zip"), Path(r"chapter15\new_extracted"))

for p in Path(r"chapter15\new_extracted\data2").glob("*.xlsx"):
    print(1)
    print(p)