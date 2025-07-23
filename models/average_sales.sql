SELECT
    EXTRACT(MONTH FROM order_date) AS month,
    EXTRACT(YEAR FROM order_date) AS year,
    ROUND(AVG(sales),2) as average_sales
FROM
    {{ ref('fact_sales') }}
GROUP BY  
    month, year
ORDER BY year ASC, month ASC