def calculate_risk(vendor):

    score = float(vendor["risk_score"])

    # Data Sensitivity
    sensitivity = str(vendor["data_sensitivity"]).upper()

    if sensitivity == "CRITICAL":
        score += 30
    elif sensitivity == "HIGH":
        score += 20
    elif sensitivity == "MEDIUM":
        score += 10

    # Breach Count
    score += min(int(vendor["breach_count"]) * 5, 20)

    # Financial Rating
    rating = str(vendor["financial_rating"]).upper()

    if rating == "C":
        score += 20
    elif rating == "C+":
        score += 15
    elif rating == "B-":
        score += 5

    # Missing Certifications
    if str(vendor["soc2_type2"]).upper() == "FALSE":
        score += 10

    if str(vendor["iso27001"]).upper() == "FALSE":
        score += 10

    # Missing GDPR
    if str(vendor["gdpr_dpa"]).upper() == "FALSE":
        score += 10

    return min(score, 100)