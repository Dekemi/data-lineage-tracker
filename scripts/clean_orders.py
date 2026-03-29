import pandas as pd
from lineage_tracker import log_lineage

df = pd.read_csv("data/raw/orders_raw.csv")

# Data cleaning
df = df.drop_duplicates()
df["quantity"] = df["quantity"].fillna(1)
df["price"] = df["price"].fillna(df["price"].mean())

df.to_csv("data/processed/orders_cleaned.csv", index=False)

# Log lineage
log_lineage("orders_raw", "orders_cleaned", "cleaning: remove duplicates, fill nulls")