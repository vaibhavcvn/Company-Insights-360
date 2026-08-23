# Company Insights 360

A data analytics and business intelligence project that combines Python, SQL, and Power BI to analyze company sales, profitability, employee performance, departments, regions, and customer purchasing patterns.

## Project Overview

Company Insights 360 transforms raw company data into actionable business insights using an end-to-end analytics workflow.

The project includes:

- Data preprocessing and conversion using Python
- Exploratory Data Analysis using Pandas and Matplotlib
- SQL-based business analysis using SQLite
- Interactive Power BI dashboards
- Business-focused KPIs and visualizations
- Exported analytical charts and dashboard screenshots

## Business Objectives

The analysis focuses on answering questions such as:

- Which regions generate the highest sales?
- Which regions and categories are most profitable?
- How do sales change over time?
- Which product categories contribute most to revenue?
- How does discounting affect profit?
- How do departments perform?
- What business areas require attention?

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data manipulation |
| Matplotlib | Exploratory data visualization |
| SQL | Business analysis and querying |
| SQLite | Local analytical database |
| Power BI | Interactive dashboards and reporting |
| Git & GitHub | Version control and project management |

## Project Structure

```text
Company-Insights-360/
|
+-- data/
|   +-- departments.csv
|   +-- departments.xls
|   +-- employees.csv
|   +-- employees.xls
|   +-- sales.csv
|   +-- sales.xls
|
+-- python/
|   +-- analysis.py
|   +-- convert_data.py
|   +-- eda.py
|
+-- SQL/
|   +-- queries.sql
|   +-- run_queries.py
|
+-- outputs/
|   +-- department_performance.png
|   +-- discount_vs_profit.png
|   +-- monthly_sales.png
|   +-- profit_by_region.png
|   +-- sales_by_category.png
|   +-- sales_by_region.png
|
+-- screenshots/
|   +-- dashboard.png
|   +-- buisness-insights.png
|
+-- Company_Insights_360.pbix
+-- requirements.txt
+-- README.md
+-- .gitignore