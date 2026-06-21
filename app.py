from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset once
df = pd.read_csv("data/raw/vendor_registry.csv")


# ======================
# DASHBOARD
# ======================
@app.route("/")
def dashboard():

    data = df.copy()

    search = request.args.get("search")
    risk = request.args.get("risk")

    if search:
        data = data[
            data["vendor_name"].str.contains(
                search,
                case=False,
                na=False
            )
            |
            data["vendor_id"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if risk:
        data = data[
            data["risk_level"] == risk
        ]

    vendors = data.to_dict("records")

    return render_template(
        "dashboard.html",
        vendors=vendors,
        total=len(df),
        high=len(df[df["risk_level"] == "HIGH"]),
        medium=len(df[df["risk_level"] == "MEDIUM"]),
        low=len(df[df["risk_level"] == "LOW"])
    )


# ======================
# VENDOR DETAILS
# ======================
@app.route("/vendor/<vendor_id>")
def vendor_details(vendor_id):

    vendor = df[
        df["vendor_id"] == vendor_id
    ]

    if vendor.empty:
        return "Vendor Not Found"

    vendor = vendor.iloc[0].to_dict()

    return render_template(
        "vendor_detail.html",
        vendor=vendor
    )


# ======================
# ALERTS PAGE
# ======================
@app.route("/alerts")
def alerts():

    high_risk = df[
        df["risk_level"] == "HIGH"
    ]

    vendors = high_risk.to_dict("records")

    return render_template(
        "alerts.html",
        vendors=vendors
    )


# ======================
# REPORTS PAGE
# ======================
@app.route("/reports")
def reports():

    compliant = len(
        df[
            (df["soc2_type2"] == True)
            &
            (df["iso27001"] == True)
        ]
    )

    compliance_percent = round(
        (compliant / len(df)) * 100,
        2
    )

    return render_template(
        "reports.html",
        total=len(df),
        high=len(df[df["risk_level"] == "HIGH"]),
        medium=len(df[df["risk_level"] == "MEDIUM"]),
        low=len(df[df["risk_level"] == "LOW"]),
        compliance_percent=compliance_percent
    )


if __name__ == "__main__":
    app.run(debug=True)