import pandas as pd


# ==========================================
# 1. LOAD DATA
# ==========================================

sales = pd.read_csv("data/sales.xls")
employees = pd.read_csv("data/employees.xls")
departments = pd.read_csv("data/departments.xls")


# ==========================================
# 2. CONVERT DATES
# ==========================================

sales["Date"] = pd.to_datetime(sales["Date"])
employees["HireDate"] = pd.to_datetime(employees["HireDate"])


# ==========================================
# 3. COMPANY-WIDE KPIs
# ==========================================

total_sales = sales["Sales"].sum()
total_profit = sales["Profit"].sum()
total_orders = sales["OrderID"].nunique()
average_order_value = sales["Sales"].mean()
profit_margin = (total_profit / total_sales) * 100
average_discount = sales["Discount"].mean() * 100

print("\n========== COMPANY KPIs ==========")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Average Discount: {average_discount:.2f}%")


# ==========================================
# 4. SALES BY REGION
# ==========================================

region_analysis = (
    sales.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("OrderID", "nunique")
    )
)

region_analysis["Profit_Margin"] = (
    region_analysis["Profit"] /
    region_analysis["Sales"] * 100
)

region_analysis = region_analysis.sort_values(
    "Sales",
    ascending=False
)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis)


# ==========================================
# 5. SALES BY CATEGORY
# ==========================================

category_analysis = (
    sales.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("OrderID", "nunique")
    )
)

category_analysis["Profit_Margin"] = (
    category_analysis["Profit"] /
    category_analysis["Sales"] * 100
)

category_analysis = category_analysis.sort_values(
    "Sales",
    ascending=False
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_analysis)


# ==========================================
# 6. EMPLOYEE PERFORMANCE BY DEPARTMENT
# ==========================================

department_performance = (
    employees.groupby("Department")
    .agg(
        Average_Performance=("PerformanceScore", "mean"),
        Average_Salary=("Salary", "mean"),
        Employees=("EmployeeID", "count"),
        Average_Experience=("Experience", "mean")
    )
)

department_performance = department_performance.sort_values(
    "Average_Performance",
    ascending=False
)

print("\n========== DEPARTMENT PERFORMANCE ==========")
print(department_performance)


# ==========================================
# 7. DISCOUNT ANALYSIS
# ==========================================

sales["Discount_Group"] = pd.cut(
    sales["Discount"],
    bins=[-0.01, 0.05, 0.10, 0.15, 0.20],
    labels=["0-5%", "5-10%", "10-15%", "15-20%"]
)

discount_analysis = (
    sales.groupby("Discount_Group", observed=True)
    .agg(
        Average_Sales=("Sales", "mean"),
        Average_Profit=("Profit", "mean"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("OrderID", "count")
    )
)

discount_analysis["Profit_Margin"] = (
    discount_analysis["Total_Profit"] /
    discount_analysis["Total_Sales"] * 100
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)


# ==========================================
# 8. HIGH-DISCOUNT VS LOW-DISCOUNT
# ==========================================

low_discount = sales[sales["Discount"] <= 0.15]
high_discount = sales[sales["Discount"] > 0.15]

print("\n========== HIGH VS LOW DISCOUNT ==========")

print(
    f"Average profit (discount <= 15%): "
    f"${low_discount['Profit'].mean():,.2f}"
)

print(
    f"Average profit (discount > 15%): "
    f"${high_discount['Profit'].mean():,.2f}"
)

profit_change = (
    (high_discount["Profit"].mean() -
     low_discount["Profit"].mean())
    / low_discount["Profit"].mean()
) * 100

print(f"Profit change: {profit_change:.2f}%")


# ==========================================
# 9. SALES BY DEPARTMENT
# ==========================================

sales_employee = sales.merge(
    employees[["EmployeeID", "Department"]],
    on="EmployeeID",
    how="left"
)

department_sales = (
    sales_employee.groupby("Department")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("OrderID", "nunique")
    )
)

department_sales["Profit_Margin"] = (
    department_sales["Profit"] /
    department_sales["Sales"] * 100
)

print("\n========== SALES BY DEPARTMENT ==========")
print(department_sales.sort_values("Sales", ascending=False))