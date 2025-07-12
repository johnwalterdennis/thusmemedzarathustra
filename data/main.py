import pandas as pd

df=pd.read_csv("chapternames.csv")

# first_col = df.columns[0]
# df[first_col] = (
#     df[first_col]
#         .astype(str)           
#         .str.split(" ", n=1)
#         .str[1]               
#         .fillna("")           
# )

first_col = df.columns[0]
df[first_col] = (
    df[first_col]
      .astype(str)                    # be sure we’re working with strings
      .str.replace(r"\.\s*$", "", regex=True)   # remove ".", " .", ".  " at EOL
      .str.title()                    # “on the three metamorphoses” → “On The Three Metamorphoses”
)

df.to_csv("chapternames1.csv", index=False, sep=";",encoding="utf-8", na_rep="NA")

print(df.head())
