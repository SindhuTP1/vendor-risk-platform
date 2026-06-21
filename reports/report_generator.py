import pandas as pd

df = pd.read_csv("data/raw/vendor_registry.csv")

high_risk = df[df["risk_level"] == "HIGH"]

high_risk.to_csv(
    "reports/high_risk_vendors.csv",
    index=False
)

print("Report Generated")