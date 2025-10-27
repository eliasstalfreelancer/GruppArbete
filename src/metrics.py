
"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""
import src.io_utils as io_utils
import pandas as pd
import src.ecommerce as ecommerce

class DataProccesing:
    def __init__(self,path):
        data = io_utils.load_data(path)
        clean_data = io_utils.clean_data(data)
        clean_data_df = pd.DataFrame(clean_data)
        #exmpel på hur man kallar fram en variable som liger i self:
        #DataProccesing("data/ecommerce_sales.csv").amount_of_orders_df
        self.clean_data_df = clean_data_df
        
    def key_words(self):
        avo = ecommerce.average_vaule_order(df=self.clean_data_df)
        revenue = ecommerce.total_index(df=self.clean_data_df,index="revenue")
        unints =  ecommerce.total_index(df=self.clean_data_df,index="units")
        orders = ecommerce.amount_of_orders(df=self.clean_data_df)
    
        
        
        return print(f"Aov: {avo} kr per order. {"\n"}Antalet ordrar: {orders} st. {"\n"}Inkomst: {revenue} kr. {"\n"}Antal enheter: {unints} st.")
        




"""Här vill vi smala alla uträkningar som vi ska använda för att sedan skapa diagram i viz.py"""

