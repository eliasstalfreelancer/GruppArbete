import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv(
    'C:/Users/chn03/Desktop/Python lessons/EC utbildning/ecommerce_sales.csv', header=0)
print(data.head())


# table of city
print("Columns:", data.columns.tolist())

print(data.columns)


counts_city = data['city'].value_counts()
print(counts_city)

counts_category = data['category'].value_counts()
print(counts_category)


# average revenue by category
print(data.groupby('category')['revenue'].mean().round(2))

# average revenue by city
print(data.groupby('city')['revenue'].mean().round(2))

# number of units per category
print(data.groupby('category')['units'].sum())

# number of units per city
print(data.groupby('city')['units'].sum())


# Plots the data

# plotting average revenue by category
plot1 = sns.catplot(x='category', y='revenue', data=data, kind='box')
plt.title('Average Revenue by Category')
plt.show()

# plotting average revenue by city
plot2 = sns.catplot(x='city', y='revenue', data=data, kind='box')
plt.title('Average Revenue by City')
plt.show()

# box plot of average revenue by category and by city
plot3 = sns.catplot(x='category', y='revenue',
                    hue='city', data=data, kind='box')
plt.title('Average Revenue by Category and City')
plt.show()
