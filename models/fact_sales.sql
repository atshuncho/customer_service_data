select
    s.order_number,
    s.customer_key,
    c.first_name,
    c.last_name,
    s.product_key,
    p.product_name,
    s.order_date,
    s.sales
from `customer-data-466418.customers_dataset.sales_data` s
left join
    `customer-data-466418.customers_dataset.customer_data` c
    on s.customer_key = c.customer_key
left join
    `customer-data-466418.customers_dataset.products_data` p
    on s.product_key = p.product_key
