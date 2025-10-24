# vill att göra: ta sök ord och retunera intäker bonus mål att return top lista.

import pandas as pd
import csv


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
