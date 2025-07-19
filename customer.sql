/* 
The tables used are downloaded from kaggle.
I have analysed the tables and thought about key questions which could be asked in a data anyalst role.
*/ 
-- There are rows that are innacurate so we will remove them.
-- We know they are innacurate because the quantity * price does not =  sales

DROP TABLE IF EXISTS sales_v2;
CREATE TABLE sales_v2 AS SELECT * FROM
    sales
WHERE
    quantity * price = sales;


SELECT 
    *
FROM
    sales_v2;

-- 1. Which products generated the highest revenue over the past year?

SELECT 
  p.product_name, 
  SUM(s.sales) AS total_revenue
FROM products p
JOIN sales_v2 s ON p.product_key = s.product_key
WHERE s.order_date >= '2014-01-01'
-- As the question says the past year, I would use the code to the right, but there has not been an order since 2014: WHERE s.order_date >= CURRENT_DATE - Interval 1 YEAR
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 10;


-- 2. What is the Average Order Value (AOV) by customer segment (country, marital status, gender)
-- 2a. Country
SELECT 
    c.country, ROUND(AVG(s.sales), 2) AS average_sales_by_country
FROM
    customers c
        JOIN
    sales_v2 s ON c.customer_key = s.customer_key
GROUP BY country
ORDER BY average_sales_by_country DESC;
    
-- 2b. marital status

SELECT 
    c.marital_status, ROUND(AVG(s.sales), 2) AS average_sales_by_marital_status
FROM
    customers c
        JOIN
    sales_v2 s ON c.customer_key = s.customer_key
GROUP BY marital_status;

-- 2c. gender 

SELECT 
    c.gender, ROUND(AVG(s.sales), 2) AS average_sales_by_marital_status
FROM
    customers c
        JOIN
    sales_v2 s ON c.customer_key = s.customer_key
GROUP BY gender;

-- 3. Who are our top 10 customers by highest sale, most sales and which customers have spent the most?
-- 3a. highest sales
SELECT
	c.customer_key, CONCAT(c.first_name, ' ', c.last_name) AS name, s.sales
FROM 
	customers c
		JOIN 
	sales_v2 s ON s.customer_key = c.customer_key
ORDER BY sales DESC
LIMIT 10;
-- 3b. most sales

SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS name, c.customer_key, COUNT(s.customer_key) AS amount_of_sales
FROM 
	customers c
		JOIN 
	sales_v2 s ON s.customer_key = c.customer_key
GROUP BY customer_key
ORDER BY amount_of_sales DESC
LIMIT 10;

-- 3c. Which customers have spent the most

SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS name, c.customer_key, SUM(s.sales) as total_sales 
FROM 
	customers c
		JOIN
	sales_v2 s ON c.customer_key = s.customer_key
		
GROUP BY customer_key
ORDER BY total_sales DESC
LIMIT 10;

-- 4.How has sales performance changed month over month?
-- Average revenue
-- Monthly total revenue

SELECT 
    MONTH(order_date) AS month,
    YEAR(order_date) AS year,
    AVG(sales),
    SUM(sales) AS total_sales
FROM
    sales_v2
GROUP BY month , year
ORDER BY year DESC , month DESC;

-- 5.What is the average lead time between order date and shipping date by month?
SELECT
	MONTH(order_date) AS month,
    YEAR(order_date) AS YEAR,
    AVG(DATEDIFF(due_date, order_date)) AS time -- due date has been used as there is no column for actual date received.
FROM
	sales_v2
GROUP BY month, year
ORDER BY year, month;

-- 6. Which products are most frequently ordered together?

SELECT
	p_1.product_name AS product_1_name,
	a.product_key AS product_1_id,
    p_2.product_name AS product_2_name,
    b.product_key AS product_2_id,
    COUNT(*) AS times_ordered_together
FROM
	sales_v2 a
		JOIN
	sales_v2 b ON a.order_number = b.order_number AND a.product_key < b.product_key -- Used to make sure duplicates are remove
		JOIN
	products p_1 ON p_1.product_key = a.product_key
		JOIN
	products p_2 ON p_2.product_key = b.product_key
GROUP BY a.product_key, b.product_key
ORDER BY times_ordered_together DESC
LIMIT 10;

-- 7. How many customers are repeat vs one-time buyers?

SELECT 
	customer_key,
    COUNT(*) AS num_orders
FROM sales_v2
GROUP BY customer_key;

SELECT
	CASE
		WHEN num_orders = 1 THEN 'one_time_buyer'
        ELSE 'repeat buyer'
	END AS buyer_type,
    COUNT(*) AS num_customers

	














	
    







