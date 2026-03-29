import pandas as pd
from lineage_tracker import log_lineage

orders = pd.read_csv("data/processed/orders_cleaned.csv")

orders["revenue"] = orders["quantity"] * orders["price"]

summary = orders.groupby("customer_id")["revenue"].sum().reset_index()

summary.to_csv("data/processed/revenue_summary.csv", index=False)

log_lineage("orders_cleaned", "revenue_summary", "aggregate revenue per customer")