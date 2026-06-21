import pandas as pd
from datetime import datetime

df = pd.read_csv("data/raw/vendor_registry.csv")

today = datetime.now()

alerts = []

for _, row in df.iterrows():

    try:
        contract_end = pd.to_datetime(row["contract_end_date"])

        days_left = (contract_end - today).days

        if days_left < 0:
            alerts.append(
                f"{row['vendor_id']} Contract EXPIRED {-days_left} days ago"
            )

        elif days_left <= 60:
            alerts.append(
                f"{row['vendor_id']} Contract expiring in {days_left} days"
            )

    except:
        pass

print("Total Alerts:", len(alerts))

for alert in alerts[:20]:
    print(alert)