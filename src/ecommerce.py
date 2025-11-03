"""Läs in funktioner från metrics"""



import pandas as pd
#används för att få ut summan av enheter och intäkt

import src.metrics as me


class DataProccesing:
    def __init__(self,df):
        self.clean_data_df = df
        
    def key_words(self):
        avo = me.average_vaule_order(df=self.clean_data_df)
        revenue = me.total_index(df=self.clean_data_df,index="revenue")
        unints =  me.total_index(df=self.clean_data_df,index="units")
        orders = me.amount_of_orders(df=self.clean_data_df)
    
        
        
        return print(f"Aov: {avo} kr per order. \nAntalet ordrar: {orders} st. \nInkomst: {revenue} kr. \nAntal enheter: {unints} st.")
        

  
        
        
   

    





"""Skapar vi en klass som hämtar värden från metrics.
Klassen ska retunera våra nyckelvärden, förslagvis:
- Antal ordrar
- Total antal enheter
- Medelordervärde (AVO)
- Total intäkt"""