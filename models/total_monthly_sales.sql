SELECT
    EXTRACT(MONTH FROM order_date) AS month,
    EXTRACT(YEAR FROM order_date) AS year,
    ROUND(SUM(sales),2) as total_sales
FROM
    {{ ref('fact_sales') }}
GROUP BY  
    month, year
ORDER BY year ASC, month ASC