# Customer Analytics Project

This project explores customer purchasing behaviour through cleaned and transformed datasets in BigQuery using dbt. It includes end-to-end data modeling, testing, and dashboarding in Looker Studio to enable customer segmentation, repeat buyer analysis, and revenue insights.

---

## Tools Used

- **dbt Cloud** – for data transformation, testing, version control, and model documentation  
- **Google BigQuery** – cloud data warehouse for querying and storing models  
- **Google Looker Studio** – dashboarding and visual analytics  
- **SQL** – dbt models and transformations (BigQuery SQL)  
- **Git & GitHub** – version control and collaboration  
- **Python (pandas, itertools)** – used for additional analysis


# Customer Service Data Analysis Project

This project explores customer purchasing behavior using SQL and dbt (Data Build Tool). It combines and transforms raw sales, product, and customer data into clean, tested, and insightful datasets for analysis and dashboarding.

## Objective

To generate actionable insights on:
- **Top spending customers**
- **Product sales trends**
- **Customer segmentation**
- **Repeat buyer behavior**

These insights are visualized in **Looker Studio** to help stakeholders understand customer value and sales performance.
[View Dashboard](https://lookerstudio.google.com/reporting/0fa75936-66b1-4874-870b-a6129cfee1f7)

---


## Dashboards Overview 
[View Dashboard](https://lookerstudio.google.com/reporting/0fa75936-66b1-4874-870b-a6129cfee1f7)



| Folder             | Description                                                  |
|--------------------|--------------------------------------------------------------|
| `models/`          | All dbt models used to transform and clean the data          |
| `tests/`           | dbt tests for data quality (e.g., not null, unique)          |
| `seeds/`           | Seed files used to load data into dbt                        |
| `snapshots/`       | dbt snapshots for tracking slowly changing dimensions        |
| `screenshots/`     | Stored Looker Studio dashboard images                        |
| `python/`          | Additional Python scripts for customer insights              |

---

## DBT Models Built

Below are some of the dbt models and their business purpose:

| Model                         | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `fact_sales.sql`             | products_data.sql, customer_data.sql and sales_data.sql merged together for simple reference                                           |
| `products_data.sql`          | Cleaned product data for joins and aggregation                             |
| `customer_data.sql`          | Cleaned customer profile dataset                                            |
| `top_customers_by_sale.sql`  | Shows the top 10 customers by total sales                                   |
| `repeat_buyers.sql`          | Identifies customers who ordered more than once                             |
| `average_sales.sql`          | Calculates average sales across all orders                                  |
| `total_monthly_sales.sql`    | Total sales grouped by month and year (used for time-series visualisation) |

Each model is defined in `models/`, versioned, and tested using schema.yml for quality control.

---

## DBT Testing & Documentation

I have implemented:

- **Schema tests**: `not_null`, `unique` on key fields (e.g., `customer_key`)
- **Descriptive metadata**: All models and columns have descriptions
- **Version control**: dbt changes are committed to GitHub (`patch-1` branch)

---

## Dashboard: Customer Sales Overview

Built in **Looker Studio**, includes:

- Total Customers
- Sales Volume
- Repeat Buyers
- Most Popular Products
- Monthly Revenue Trends
- Filter by Country, Year, Month

Data is sourced from BigQuery views generated from my dbt models.

<p float="left">
  <img src="screenshots/looker_studio_product_sales.png" width="400" />
  <img src="screenshots/looker_studio_customer_breakdown.png" width="400" />
</p>

---

## Workflow

1. Load raw CSV data using `seeds/`
2. Transform data in **dbt Cloud**
3. Run **tests** and **build models**
4. Commit updates to **GitHub**
5. Query cleaned data in **BigQuery**
6. Visualise in **Looker Studio**

| Folder | Description |
|--------|-------------|
| `models/` | dbt models – raw and transformed SQL files |
| `seeds/` | CSV seed files ingested into BigQuery |
| `tests/` | dbt tests and assertions for model quality |
| `snapshots/` | Historical data snapshots (for slowly changing dimensions|
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
```
---

## Questions Answered on Python Script and MySQL

1. **Which products generated the highest revenue over the past year?
2. **What is the Average Order Value (AOV) by customer segment (country, marital status, gender)
3. **Who are our top 10 customers by highest sale, most sales and which customers have spent the most?
4. **.How has sales performance changed month over month? Average and Total.
5. **What is the average lead time between order date and shipping date by month?
6. **Which products are most frequently ordered together?
7. **How many customers are repeat vs one-time buyers?


[Python Script](https://github.com/atshuncho/customer_service_data/blob/main/python/customer_insights.py)
[MySQL Script](https://github.com/atshuncho/customer_service_data/blob/main/sql/customer.sql) 
