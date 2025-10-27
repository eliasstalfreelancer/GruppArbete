"""Läs in funktioner från metrics"""



import pandas as pd
#används för att få ut summan av enheter och intäkt

def amount_of_orders(df):
    
    amount_of_orders = len(df) 

    return amount_of_orders


def total_index(df,index):
    sum = df[index].sum()
    rounded_sum = sum.round(2)
        
    return rounded_sum

def average_vaule_order(df):
    revenue = total_index(df,"revenue")
    orders = amount_of_orders(df)
    aov = revenue/orders
    rounded_aov = aov.round(2)
    
    return rounded_aov  
  
        
        
   

    





"""Skapar vi en klass som hämtar värden från metrics.
Klassen ska retunera våra nyckelvärden, förslagvis:
- Antal ordrar
- Total antal enheter
- Medelordervärde (AVO)
- Total intäkt"""