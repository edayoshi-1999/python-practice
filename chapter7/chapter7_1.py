import pandas as pd

# data_by_list = [
#     ["スパム", 500, 3],
#     ["卵", 168, 8],
#     ["ベーコン", 1250, 1]
# ]
# df_by_list = pd.DataFrame(data_by_list)
# print(df_by_list)

# data_by_dict = {
#     "名前": ["スパム", "卵", "ベーコン"],
#     "単価": [500, 168, 1250],
#     "個数": [3, 8, 1]
# }
# index = ["one", "two", "three"]
# df_by_dict = pd.DataFrame(data_by_dict, index=index)
# print(df_by_dict)

# df = pd.read_csv(r"chapter7\data\data1.csv")
# print(df)

# df = pd.read_csv(r"chapter7\data\data1.csv")
# print(df)
# print(df.info(), end="\n\n")
# print(df.describe(), end="\n\n")
# print(df.head(2))
# print(df.sample(2))
# print(df.tail(2))
# print(df.T.head(2))
# print(df.index)
# print(df.columns)
# values = df.values
# print(type(values))
# print(values)

# data = {
#     "名前": ["スパム", "卵", "ベーコン"],
#     "単価": [500, 168, 1250],
#     "個数": [3, 8, 1]
# }
# df = pd.DataFrame(data)
# df.to_csv(r"chapter7\food.csv")
# df.to_csv(r"chapter7\food.csv", header=False, index=False, mode="a")
# df.to_excel(r"chapter7\food.xlsx", sheet_name="シート1")