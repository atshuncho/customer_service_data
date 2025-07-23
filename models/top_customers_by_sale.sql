SELECT
  customer_key,
  SUM(sales) AS total_sales
FROM {{ ref('fact_sales') }}
GROUP BY customer_key
ORDER BY total_sales DESC