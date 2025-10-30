
import pandas as pd

"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""


"""Här vill vi smala alla uträkningar som vi ska använda för att sedan skapa diagram i viz.py"""


def groupby_category(df):
    """
    Gruperar per categori och räknar: antal, medelvärde och summa för 'revenue' i varje grupp
    """    
    return (
        df.groupby('category', observed=False)['revenue']
        .agg(antal='count', medel='mean', total='sum', std= 'std')
        .sort_values(by='total', ascending=False)
        .reset_index()
        ) 