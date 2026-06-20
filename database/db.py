import sqlite3

DATABASE = "vendor_risk.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    return conn