import pandas as pd

df = pd.read_csv("data/raw/vendor_registry.csv")

print("\nRisk Level Distribution:")
print(df["risk_level"].value_counts())

print("\nData Sensitivity Distribution:")
print(df["data_sensitivity"].value_counts())

print("\nFinancial Rating Distribution:")
print(df["financial_rating"].value_counts())