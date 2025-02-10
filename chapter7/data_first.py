import pathlib
import pandas as pd

my_path = pathlib.Path(r"chapter7\data")

df = pd.DataFrame()
for p in my_path.glob("*.csv"):
    df_current = pd.read_csv(p)
    df = pd.concat([df, df_current], ignore_index=True)

df.to_excel(r"chapter7\data\data.xlsx")
