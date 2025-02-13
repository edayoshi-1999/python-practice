import shutil
from pathlib import Path



def copy_with_organizing(from_path, to_path):
    to_path.mkdir()
    for p in from_path.glob("**/*"):
        suffix = p.suffix[1:]
        dir = to_path / suffix

        if p.is_file():
            dir.mkdir(exist_ok=True)
            shutil.copy2(p, dir)
    
extracted = Path(r"chapter15\extracted")
organized = Path(r"chapter15\organized")

# 解答
shutil.unpack_archive(r"chapter15\data.zip", extracted)

# ファイルの拡張子ごとにフォルダを作ってその中にコピー
copy_with_organizing(extracted, organized)

# 上記の新しいフォルダを圧縮
shutil.make_archive(r"chapter15\archive", "zip", organized)