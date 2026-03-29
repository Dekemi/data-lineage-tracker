import sqlite3
import pandas as pd
import networkx as nx

conn = sqlite3.connect("db/lineage.db")
df = pd.read_sql("SELECT * FROM lineage", conn)

G = nx.DiGraph()

for _, row in df.iterrows():
    G.add_edge(row["source"], row["target"])

print("Nodes:", G.nodes())
print("Edges:", G.edges())

print("Downstream of orders_raw:", list(nx.descendants(G, "orders_raw")))