from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():

    df = pd.read_csv(
        "data/raw/vendor_registry.csv"
    )

    vendors = df.to_dict("records")

    return render_template(
        "dashboard.html",
        vendors=vendors
    )

if __name__ == "__main__":
    app.run(debug=True)