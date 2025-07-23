# Customer Service Data Analysis Project

This project explores customer purchasing behavior using SQL and dbt (Data Build Tool). It combines and transforms raw sales, product, and customer data into clean, tested, and insightful datasets for analysis and dashboarding.

## Objective

To generate actionable insights on:
- **Top spending customers**
- **Product sales trends**
- **Customer segmentation**
- **Repeat buyer behavior**

These insights are visualized in **Looker Studio** to help stakeholders understand customer value and sales performance.

---

## Project Structure

| Folder | Description |
|--------|-------------|
| `models/` | dbt models – raw and transformed SQL files |
| `seeds/` | CSV seed files ingested into BigQuery |
| `tests/` | dbt tests and assertions for model quality |
| `snapshots/` | Historical data snapshots (for slowly changing dimensions – optional) |
| `analyses/` | Ad hoc SQL scripts and deep dives |
| `macros/` | Reusable SQL functions (Jinja templates) |
| `python/` | Python scripts for data processing or EDA |
| `screenshots/` | Project images and documentation examples |

---

## Data Pipeline Overview

1. **Seeded raw data** (`sales`, `products`, `customers`) into BigQuery.
2. **Joined datasets** in the `fact_sales.sql` model using dbt.
3. Built a **summary model**: `top_customers_by_sale.sql` to show highest value customers.
4. Created a **YAML schema file** to:
   - Document models and columns
   - Add automated tests (e.g., `not_null`, `unique`)
5. **Built models using dbt CLI / dbt Cloud**.
6. **Tested** model assumptions using `dbt test`.
7. **Deployed** transformations to BigQuery and versioned changes in GitHub.

---

## Example: `top_customers_by_sale`

Shows the top 10 customers by total sales.

```sql
SELECT
  customer_key,
  SUM(sales) AS total_sales
FROM {{ ref('fact_sales') }}
GROUP BY customer_key
ORDER BY total_sales DESC
LIMIT 10
