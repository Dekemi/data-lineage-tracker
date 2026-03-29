import streamlit as st
import networkx as nx
import sqlite3
import pandas as pd

st.title("Data Lineage Tracker")

conn = sqlite3.connect("db/lineage.db")
df = pd.read_sql("SELECT * FROM lineage", conn)

G = nx.DiGraph()

for _, row in df.iterrows():
    G.add_edge(row["source"], row["target"])

table = st.selectbox("Select Table", list(G.nodes))

st.write("### Downstream Impact")
st.write(list(nx.descendants(G, table)))

st.write("### Upstream Sources")
st.write(list(nx.ancestors(G, table)))