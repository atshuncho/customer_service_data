SELECT
    customer_key,
    COUNT(order_number) AS amount_of_orders
FROM {{ ref('fact_sales') }}
GROUP BY customer_key
HAVING amount_of_orders > 1
ORDER BY amount_of_orders DESC