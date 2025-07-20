# Python Analysis – Customer Service Dataset

This folder contains a Python-based analysis of the same customer dataset using `pandas`. The notebook/script mirrors the logic in the SQL queries to demonstrate equivalence between SQL and programmatic analysis.

---

## Files

- `analysis.py` – All logic and data transformation done in one file
- `customers.csv`, `sales.csv`, `products.csv` – Dataset files

---

## Key Business Questions Answered

1. **Top 10 revenue-generating products**
   - Merged `sales` with `products`, grouped by `product_name`

2. **Average Order Value (AOV) by segment**
   - Segments: `country`, `marital_status`, `gender`

3. **Top customers**
   - Highest single sale  
   - Most number of sales  
   - Total spending

4. **Sales performance over time**
   - Monthly `SUM(sales)` and `AVG(sales)` visualized over time

5. **Average lead time (order to delivery)**
   - `due_date - order_date` aggregated by month

6. **Products frequently bought together**
   - Combinations of `product_name` in shared `order_number`

7. **Repeat vs one-time customers**
   - Classified using `num_orders > 1`

---

## Techniques Used

- `pandas` for data wrangling and transformation
- `itertools.combinations` for product pairs
- `Counter` from `collections` for frequency analysis

---

## Requirements

- Python 3.7+
- pandas
