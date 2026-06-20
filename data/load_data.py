import pandas as pd
import sqlite3

# Database connection
conn = sqlite3.connect("vendor_risk.db")

# Read CSV files
vendors = pd.read_csv("data/raw/vendor_registry.csv")
labels = pd.read_csv("data/raw/vendor_labels.csv")

# Store into SQLite
vendors.to_sql("vendors", conn, if_exists="replace", index=False)
labels.to_sql("vendor_labels", conn, if_exists="replace", index=False)

print("Data loaded successfully!")

# Check records
print("Vendor Records:", len(vendors))
print("Label Records:", len(labels))

conn.close()