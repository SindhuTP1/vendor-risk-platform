import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/raw/vendor_registry.csv"
)

risk_counts = df[
    "risk_level"
].value_counts()

plt.figure(figsize=(6,6))

risk_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "Vendor Risk Distribution"
)

plt.savefig(
    "static/risk_chart.png"
)

print("Chart Created")