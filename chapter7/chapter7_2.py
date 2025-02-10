# from pathlib import Path
import subprocess

# p_dir = Path(r"chapter7")
# for p in (p_dir / "data").iterdir():
#     print(p)
# for p in p_dir.glob("**/*.xlsx"):
#     print(p)
# for p in p_dir.glob("**/data[1|3].csv"):
#     print(p)

excel = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
subprocess.Popen(excel)