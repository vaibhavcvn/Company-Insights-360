import sqlite3
from pathlib import Path
import pandas as pd


# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "company_insights.db"


# Connect to database
connection = sqlite3.connect(DATABASE_PATH)


# ==========================================
# COMPANY KPIs
# ==========================================

query = """
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT OrderID) AS Total_Orders,
    ROUND(AVG(Sales), 2) AS Average_Order_Value,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin,
    ROUND(AVG(Discount) * 100, 2) AS Average_Discount
FROM sales;
"""

result = pd.read_sql_query(query, connection)

print("\n========== COMPANY KPIs ==========")
print(result.to_string(index=False))


# ==========================================
# REGION ANALYSIS
# ==========================================

query = """
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT OrderID) AS Orders,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== REGION ANALYSIS ==========")
print(result.to_string(index=False))


# ==========================================
# CATEGORY ANALYSIS
# ==========================================

query = """
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT OrderID) AS Orders,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== CATEGORY ANALYSIS ==========")
print(result.to_string(index=False))


# ==========================================
# DEPARTMENT PERFORMANCE
# ==========================================

query = """
SELECT
    Department,
    COUNT(EmployeeID) AS Employee_Count,
    ROUND(AVG(PerformanceScore), 2) AS Average_Performance,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    ROUND(AVG(Experience), 2) AS Average_Experience
FROM employees
GROUP BY Department
ORDER BY Average_Performance DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== DEPARTMENT PERFORMANCE ==========")
print(result.to_string(index=False))


# ==========================================
# SALES BY DEPARTMENT
# ==========================================

query = """
SELECT
    e.Department,
    ROUND(SUM(s.Sales), 2) AS Total_Sales,
    ROUND(SUM(s.Profit), 2) AS Total_Profit,
    COUNT(DISTINCT s.OrderID) AS Orders,
    ROUND(SUM(s.Profit) * 100.0 / SUM(s.Sales), 2) AS Profit_Margin
FROM sales s
JOIN employees e
    ON s.EmployeeID = e.EmployeeID
GROUP BY e.Department
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== SALES BY DEPARTMENT ==========")
print(result.to_string(index=False))


# Close connection
connection.close()

print("\nSQL analysis completed successfully!")