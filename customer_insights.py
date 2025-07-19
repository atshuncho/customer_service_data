'''
The tables used are downloaded from kaggle.
I have analysed the tables and thought about key questions which could be asked in a data anyalst role.
The code below answers those questions using pandas.
I first answered the questions using SQL, but then I thought it would be more fun to do it in pandas.
'''

import pandas as pd
from itertools import combinations
from collections import Counter


# Load the datasets
customers_df = pd.read_csv('customers.csv', encoding='ISO-8859-1')  

products_df = pd.read_csv('products.csv', encoding='ISO-8859-1')

sales_df = pd.read_csv('sales.csv', encoding='ISO-8859-1')

# There are rows that are innacurate so we will remove them.
# We know they are innacurate because the quantity * price does not =  sales
sales_df = sales_df[sales_df['quantity'] * sales_df['price'] == sales_df['sales']]

# 1. Which products generated the highest revenue over the past year?
highest_revenue_products = (
    sales_df.merge(products_df, on='product_key')
    .groupby('product_name')['sales']
    .sum()
    .reset_index(name='total_revenue')
    .sort_values(by='total_revenue', ascending=False)
    .head(10)
)
print("Top 10 products by revenue:")
print(highest_revenue_products)

# 2. What is the Average Order Value (AOV) by customer segment (country, marital status, gender)
# 2a. Country
aov_by_country = (
    sales_df.merge(customers_df, on='customer_key')
    .groupby('country')['sales']
    .mean()
    .reset_index(name='average_order_value')
    .sort_values(by='average_order_value', ascending=False)
)
print("\nAverage Order Value by Country:")
print(aov_by_country.round(2))

# 2b. Marital Status
aov_by_marital_status = (
    sales_df.merge(customers_df, on='customer_key')
    .groupby('marital_status')['sales']
    .mean()
    .reset_index(name='average_order_value')
    .sort_values(by='average_order_value', ascending=False)
)
print("\nAverage Order Value by Marital Status:")
print(aov_by_marital_status.round(2))

# 2c. gender   
aov_by_gender = (
    sales_df.merge(customers_df, on='customer_key')
    .groupby('gender')['sales']
    .mean()
    .reset_index(name='average_order_value')
    .sort_values(by='average_order_value', ascending=False)
)
print("\nAverage Order Value by gender:")
print(aov_by_gender.round(2))

# 3. Who are our top 10 customers by highest sale, most sales and which customers have spent the most?
# 3a. highest sales
top_customers_by_sales = (
    sales_df.merge(customers_df, on='customer_key')   
)
top_customers_by_sales['name'] = top_customers_by_sales['first_name'] + ' ' + top_customers_by_sales['last_name']
print("\nTop 10 customers by highest sales:")
print(top_customers_by_sales[['name', 'sales']].sort_values(by='sales', ascending=False).head(10)) # There are more than 10 customers with the same sales value, so we will just show the top 10.
# 3b. most sales
top_customers_by_most_sales = (
    sales_df.merge(customers_df, on='customer_key')
)
# Create full name
top_customers_by_most_sales['name'] = top_customers_by_most_sales['first_name'] + ' ' + top_customers_by_most_sales['last_name']

# Group by customer and count sales
top_customers_by_count = (
    top_customers_by_most_sales.groupby(['customer_key', 'name'])
    .size()
    .reset_index(name='amount_of_sales')
    .sort_values(by='amount_of_sales', ascending=False)
    .head(10)
)

print("Top 10 Customers by Number of Sales:")
print(top_customers_by_count.sort_values(by='amount_of_sales', ascending=False))

# 3c. most spent
top_customers_by_most_spent = sales_df.merge(customers_df, on='customer_key')

# Create full name
top_customers_by_most_spent['name'] = top_customers_by_most_spent['first_name'] + ' ' + top_customers_by_most_spent['last_name']

# Group by customer and sum sales
top_customers_by_spend = (
    top_customers_by_most_spent.groupby(['customer_key', 'name'])['sales']
    .sum()
    .reset_index(name='total_sales')
    .sort_values(by='total_sales', ascending=False)
    .head(10)
)

print("Top 10 Customers by Most Spent:")
print(top_customers_by_spend)

# 4.How has sales performance changed month over month?
# Average revenue
# Monthly total revenue

# Ensure 'order_date' is datetime
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])

# Extract year and month
sales_df['year'] = sales_df['order_date'].dt.year
sales_df['month'] = sales_df['order_date'].dt.month

# Group by year and month, then calculate metrics
monthly_performance = (
    sales_df.groupby(['year', 'month'])['sales']
    .agg(average_sales='mean', total_sales='sum')
    .reset_index()
    .sort_values(by=['year', 'month'], ascending=[False, False])
)

print("Monthly Sales Performance:")
print(monthly_performance.round(2))

# 5.What is the average lead time between order date and shipping date by month?
# Make sure order_date and due_date are datetime
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
sales_df['due_date'] = pd.to_datetime(sales_df['due_date'])

# Calculate lead time in days
sales_df['lead_time'] = (sales_df['due_date'] - sales_df['order_date']).dt.days

# Extract year and month
sales_df['year'] = sales_df['order_date'].dt.year
sales_df['month'] = sales_df['order_date'].dt.month

# Group and calculate average lead time
lead_time_by_month = (
    sales_df.groupby(['year', 'month'])['lead_time']
            .mean()
            .reset_index(name='avg_lead_time_days')
            .sort_values(by=['year', 'month'])
)

print("Average Lead Time by Month:")
print(lead_time_by_month.round(2))

# 6. Which products are most frequently ordered together?

# Merge product names into sales
sales_with_names = sales_df.merge(products_df, on='product_key')

# For each order, get all product pairs (combinations of 2)
pairs = []

# Group by order number
for order_id, group in sales_with_names.groupby('order_number'):
    products = sorted(group['product_name'].unique())
    pairs += list(combinations(products, 2))

# Count frequency of each product pair
pair_counts = Counter(pairs)

# Convert to DataFrame and sort
product_pair_df = (
    pd.DataFrame(pair_counts.items(), columns=['product_pair', 'times_ordered_together'])
      .sort_values(by='times_ordered_together', ascending=False)
      .head(10)
)

print("Top 10 Product Pairs Frequently Ordered Together:")
print(product_pair_df)

# 7. How many customers are repeat vs one-time buyers?

# Step 1: Count number of orders per customer
order_counts = sales_df.groupby('customer_key').size().reset_index(name='num_orders')

# Step 2: Classify each customer
order_counts['buyer_type'] = order_counts['num_orders'].apply(
    lambda x: 'one_time_buyer' if x == 1 else 'repeat_buyer'
)

# Step 3: Count how many customers in each group
buyer_summary = order_counts['buyer_type'].value_counts().reset_index()
buyer_summary.columns = ['buyer_type', 'num_customers']

print("Repeat vs One-time Buyers:")
print(buyer_summary)











