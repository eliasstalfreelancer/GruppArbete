import csv
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('data/ecommerce_sales.csv', header=0)
print(data.head())


# table of city
print(data.info())


# total revenue by city
total_revenue_by_city = data.groupby('city')['revenue'].sum()
print(total_revenue_by_city)

# total revenue by category
total_revenue_by_category = data.groupby('category')['revenue'].sum()
print(total_revenue_by_category)

# average revenue by city
average_revenue_by_city = data.groupby('city')['revenue'].mean()
print(average_revenue_by_city)


# histogram of revenue
plt.figure(figsize=(10, 6))
plt.hist(data['revenue'], bins=30, color='salmon', edgecolor='black')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.title('Distribution of Revenue')
plt.show()

# total revenue
total_revenue = data['revenue'].sum()
print(f'Total Revenue: {total_revenue}')

# bar plot of total revenue by category
total_revenue_by_category.plot(
    kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown'], figsize=(10, 6))
plt.xlabel('Category')
plt.ylabel('Total Revenue (million)')
plt.title('Total Revenue by Category')
plt.xticks(rotation=45)
plt.show()

# bar plot of total revenue by city
total_revenue_by_city.plot(
    kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], figsize=(10, 6))
plt.xlabel('City')
plt.ylabel('Total Revenue (million)')
plt.title('Total Revenue by City')
plt.xticks(rotation=45)
plt.show()

# barplot of city
plt.figure(figsize=(10, 6))
plt.bar(data['city'], height=data['city'].value_counts())
plt.xlabel('City')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by City')
plt.show()
