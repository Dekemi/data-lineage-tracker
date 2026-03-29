import pandas as pd
from lineage_tracker import log_lineage

df = pd.read_csv("data/raw/customers_raw.csv")

df["location"] = df["location"].fillna("Unknown")

df.to_csv("data/processed/customers_cleaned.csv", index=False)

log_lineage("customers_raw", "customers_cleaned", "fill missing locations")