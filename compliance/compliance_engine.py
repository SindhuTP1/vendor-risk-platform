import pandas as pd

def check_compliance(vendor):

    issues = []

    if str(vendor["soc2_type2"]).upper() == "FALSE":
        issues.append("SOC2 Missing")

    if str(vendor["iso27001"]).upper() == "FALSE":
        issues.append("ISO27001 Missing")

    if str(vendor["gdpr_dpa"]).upper() == "FALSE":
        issues.append("GDPR DPA Missing")

    if len(issues) == 0:
        return "COMPLIANT"

    elif len(issues) <= 2:
        return "PARTIALLY COMPLIANT"

    else:
        return "NON-COMPLIANT"


if __name__ == "__main__":

    df = pd.read_csv("data/raw/vendor_registry.csv")

    df["compliance_status"] = df.apply(check_compliance, axis=1)

    print(df[["vendor_id","vendor_name","compliance_status"]].head())
