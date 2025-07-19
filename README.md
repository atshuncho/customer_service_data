# Customer Service Sales Dashboards – Looker Studio

This project contains screenshots and documentation of two dashboards built using Google Looker Studio for analyzing customer sales and product performance.

## Dashboards Overview

### 1. **Product and Sales Breakdown**
- KPIs: Total Revenue, Total Sales, Total Products, Avg Revenue per Customer
- Charts: Revenue over time, Product breakdown by country, Revenue per product

### 2. **Customer Breakdown**
- KPIs: Total Customers, Repeat Customers, Most Common Product
- Charts: Top customers by spend, Customer location map, Monthly trend of sales vs customers

## Data Sources
- `sales.csv`: Transactional data with customer_key, order_number, sales, quantity, price, dates
- `customers.csv`: Customer master data
- `products.csv`: Product master data

## Key Features
- **Custom filters**: Country, Order Month, Product Name
- **Repeat Customer Identification**: Logic based on multiple order numbers per customer
- **Calculated metrics**: Average revenue per customer, total product count, top products

## Screenshots

<img src="Screen Shot 2025-07-19 at 21.20.07.png" width="400"/>
<img src="Screen Shot 2025-07-19 at 21.20.31.png" width="400"/>

## Notes
- Created in Looker Studio (Google Data Studio)
- No SQL used – all metrics were defined using built-in visual tools

---

**Last updated**: July 19, 2025
