import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# LOAD DATA
# ==========================================

sales = pd.read_csv("data/sales.xls")
employees = pd.read_csv("data/employees.xls")

sales["Date"] = pd.to_datetime(sales["Date"])
employees["HireDate"] = pd.to_datetime(employees["HireDate"])


# ==========================================
# 1. SALES BY REGION
# ==========================================

region_sales = sales.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("outputs/sales_by_region.png")
plt.show()


# ==========================================
# 2. SALES BY CATEGORY
# ==========================================

category_sales = sales.groupby("Category")["Sales"].sum()

plt.figure(figsize=(9, 5))
category_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("outputs/sales_by_category.png")
plt.show()


# ==========================================
# 3. PROFIT BY REGION
# ==========================================

region_profit = sales.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8, 5))
region_profit.sort_values(ascending=False).plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.savefig("outputs/profit_by_region.png")
plt.show()


# ==========================================
# 4. DEPARTMENT PERFORMANCE
# ==========================================

department_performance = (
    employees.groupby("Department")["PerformanceScore"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
department_performance.plot(kind="bar")

plt.title("Average Employee Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")

plt.tight_layout()
plt.savefig("outputs/department_performance.png")
plt.show()


# ==========================================
# 5. MONTHLY SALES TREND
# ==========================================

monthly_sales = (
    sales.set_index("Date")
    .resample("ME")["Sales"]
    .sum()
)

plt.figure(figsize=(10, 5))
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.show()


# ==========================================
# 6. DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    sales["Discount"] * 100,
    sales["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount (%)")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("outputs/discount_vs_profit.png")
plt.show()


print("\nEDA completed successfully.")
print("Charts saved in the outputs folder.")