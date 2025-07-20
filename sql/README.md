# SQL Analysis – Customer Service Dataset

This folder contains SQL logic to explore customer purchasing behavior using structured queries. Each query answers a realistic business question relevant for sales and customer analytics.

---

## Data Cleaning

Before analysis, invalid rows were removed using:

```sql
CREATE TABLE sales_v2 AS
SELECT * FROM sales
WHERE quantity * price = sales;
```

This ensures consistency and integrity of revenue calculations.

---

## Key Business Questions Answered

1. **Which products generated the highest revenue?**
   - `SUM(sales)` by `product_name` in the past year

2. **What is the Average Order Value (AOV) by customer segment?**
   - Segments analyzed: `country`, `marital_status`, `gender`

3. **Who are the top customers?**
   - By highest single sale  
   - By number of sales  
   - By total revenue spent

4. **How has sales performance changed month-over-month?**
   - Uses `MONTH()` and `YEAR()` to track trends in `AVG(sales)` and `SUM(sales)`

5. **What is the average lead time from order to due date?**
   - `AVG(DATEDIFF(due_date, order_date))` by month

6. **Which products are most frequently ordered together?**
   - Self-joins based on `order_number`, grouped by product pairings

7. **How many customers are repeat vs one-time buyers?**
   - `CASE` used to classify based on `COUNT(order_number)`

---

## Techniques Used

- Joins (`JOIN`)
- Aggregations (`SUM`, `AVG`, `COUNT`)
- Grouping and sorting (`GROUP BY`, `ORDER BY`)
- Conditional logic (`CASE`)
- Date functions (`MONTH`, `YEAR`, `DATEDIFF`)

---

## File

- `customer.sql`: Contains all queries and explanations as in-line comments
