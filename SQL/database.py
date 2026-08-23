import pandas as pd
import sqlite3
from pathlib import Path


# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "sql"

DATABASE_PATH = DATABASE_DIR / "company_insights.db"


# ==========================================
# 2. LOAD DATA
# ==========================================

sales = pd.read_csv(DATA_DIR / "sales.xls")
employees = pd.read_csv(DATA_DIR / "employees.xls")
departments = pd.read_csv(DATA_DIR / "departments.xls")


# Convert dates
sales["Date"] = pd.to_datetime(sales["Date"])
employees["HireDate"] = pd.to_datetime(employees["HireDate"])


# ==========================================
# 3. CONNECT TO SQLITE
# ==========================================

connection = sqlite3.connect(DATABASE_PATH)


# ==========================================
# 4. CREATE TABLES
# ==========================================

sales.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

employees.to_sql(
    "employees",
    connection,
    if_exists="replace",
    index=False
)

departments.to_sql(
    "departments",
    connection,
    if_exists="replace",
    index=False
)


# ==========================================
# 5. VERIFY TABLES
# ==========================================

cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
""")

tables = cursor.fetchall()

print("\n========== DATABASE CREATED ==========")

for table in tables:
    print(table[0])


# ==========================================
# 6. VERIFY ROW COUNTS
# ==========================================

print("\n========== ROW COUNTS ==========")

for table in ["sales", "employees", "departments"]:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"{table}: {count}")


# ==========================================
# 7. CLOSE CONNECTION
# ==========================================

connection.close()

print("\nDatabase created successfully!")
print(f"Location: {DATABASE_PATH}")