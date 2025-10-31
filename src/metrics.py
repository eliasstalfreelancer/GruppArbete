
"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""


"""Här vill vi smala alla uträkningar som vi ska använda för att sedan skapa diagram i viz.py"""



import pandas as pd
from src.io_utils import load_data, clean_data

df = load_data("data/ecommerce_sales.csv")
df_clean = clean_data(df)

def city_revenue(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("city",observed=False)["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

#city_revenue_result = city_revenue(df_clean)
#print(city_revenue_result)