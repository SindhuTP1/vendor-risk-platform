import pandas as pd

df = pd.read_csv("data/raw/vendor_registry.csv")

print("\nRISK SUMMARY")
print(df["risk_level"].value_counts())

print("\nCATEGORY SUMMARY")
print(df["category"].value_counts())

print("\nTOP 10 HIGH RISK VENDORS")

high_risk = df.sort_values(
    by="risk_score",
    ascending=False
)

print(
    high_risk[
        ["vendor_id","vendor_name","risk_score"]
    ].head(10)
)

high_risk.to_csv(
    "reports/high_risk_vendors.csv",
    index=False
)

print("\nReport Generated Successfully")