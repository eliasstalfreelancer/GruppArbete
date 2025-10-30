
"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""
import pandas as pd

def order_per_month(df):
    """Räknar unika ordrar per månad"""
    return df.groupby('month')['order_id'].nunique().reset_index(name='num_orders') 


def order_per_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Räknar unika ordrar per veckodag"""
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return df.groupby(df['day_of_week'])['order_id'].nunique().reset_index(name='num_order_per_week').sort_values(by='day_of_week', key=lambda x: x.map({day: i for i, day in enumerate(week_days)}))



"""Här vill vi smala alla uträkningar som vi ska använda för att sedan skapa diagram i viz.py"""

