from pathlib import Path

# csv = """,名前,単価,個数
# 0,スパム,500,3
# 1,卵,168,8
# 2,ベーコン,1250,1"""
# f = open(r"chapter14\food.csv", "w", encoding="utf-8")
# f.write(csv)
# f.close()
# f = open(r"chapter14\food.csv", "r", encoding="utf-8")
# print(f.read())
# f.close()

# p = Path(r"chapter14\pdf\aa.pdf")
# f = p.open("rb")
# binary = f.read()
# print(type(binary))
# f.close()
# p = Path(r"chapter14\test.pdf")
# f = p.open("wb")
# f.write(binary)
# f.close()

with open(r"chapter14\food.csv", "r", encoding="utf-8") as f:
    print(f.read())

with Path(r"chapter14\pdf\スキャンした書類.pdf").open("rb") as f:
    binary = f.read()
    print(type(binary))