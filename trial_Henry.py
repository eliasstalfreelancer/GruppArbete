import csv
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


# old code
# vill att göra: ta sök ord och retunera intäker bonus mål att return top lista.


class ReveuneAnylist:
    def __init__(self, file):
        with open(file, "r", encoding="utf-8") as file:
            dict_reader = csv.DictReader(file)
            contents = []
            for row in dict_reader:
                contents.append(row)
            self.dict_contents_list = contents


print(ReveuneAnylist("data/ecommerce_sales.csv").dict_contents_list)

data = pd.DataFrame(ReveuneAnylist(
    "data/ecommerce_sales.csv").dict_contents_list)
print(data)

print(data.info())
data['revenue'] = data['revenue'].astype(float)
data['category'] = data['category'].astype('category')

print(data.info())

# Var säljer vi? – vilka städer står för störst intäkt?
print(data['city'].value_counts())
print(data.groupby('city')['revenue'].sum())


print(data.groupby(['city', 'category'])['revenue'].sum())
