from load_data import load_meetings

df = load_meetings("../data/raw")

print(df.head())
print(df.columns)
print(df.shape)