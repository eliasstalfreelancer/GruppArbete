
"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""
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
  
        
        
   




"""Här vill vi smala alla uträkningar som vi ska använda för att sedan skapa diagram i viz.py"""

