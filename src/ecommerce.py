"""Läs in funktioner från metrics"""



import pandas as pd
#används för att få ut summan av enheter och intäkt

def amount_of_orders(df):
    
    amount_of_orders = df.groupby("city",observed=False)["revenue"].count()
    amount_of_orders_df = pd.DataFrame(amount_of_orders)
    amount_of_orders_df = amount_of_orders_df.rename(columns={"revenue": "Amount of orders"})
    return amount_of_orders_df

def totel_index_from_difrent_cuntries(df,index):
    sum = df.groupby("city").agg(index_sum = (index,"sum")).sort_values("index_sum",ascending=False)
        
    return sum

def average_vaule_order(df):
        
    avo = df.groupby("city",observed=False)["revenue"].mean()
    avo_df = pd.DataFrame(avo)
    avo_df = avo_df.round(2)
    avo_df = avo_df.rename(columns={"revenue": "AVO"})
        
        
    return avo_df

    





"""Skapar vi en klass som hämtar värden från metrics.
Klassen ska retunera våra nyckelvärden, förslagvis:
- Antal ordrar
- Total antal enheter
- Medelordervärde (AVO)
- Total intäkt"""