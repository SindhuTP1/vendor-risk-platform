import sqlite3
import pandas as pd

from rules import calculate_risk

conn = sqlite3.connect("vendor_risk.db")

vendors = pd.read_sql_query(
    "SELECT * FROM vendors",
    conn
)

vendors["calculated_risk_score"] = vendors.apply(
    calculate_risk,
    axis=1
)

def get_level(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 65:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    else:
        return "LOW"

vendors["calculated_risk_level"] = vendors[
    "calculated_risk_score"
].apply(get_level)

print(vendors["calculated_risk_level"].value_counts())
conn.close()