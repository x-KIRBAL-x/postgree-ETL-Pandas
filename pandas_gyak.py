import pandas as pd
df = pd.read_csv('adat.txt', sep=";")
df["#datum"] = pd.to_datetime(df["#datum"])
df2 = df.where(df["#datum"].dt.year == 2014)
months = df["#datum"].dt.month
years = df["#datum"].dt.year

print("Hónapok átlagos napi átlaghőmérsékletei:")

db = 0
for i in years:
    db += 1
print(db)
print(years.iloc[1])
#print(df.groupby(months)["d_ta"].mean())
#print(df.iloc[1])
print(df.where(df["#datum"].dt.year > 2016).groupby(years)["d_ta"].mean())

'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print("\nA legmelegebb nap:")
  display(df[df["d_ta"] == df["d_ta"].max()])'''