"""Läs in funktioner från metrics"""


import src.io_utils as io_utils
import pandas as pd
import src.metrics as metrics

class DataProccesing:
    def __init__(self,path):
        data = io_utils.load_data(path)
        clean_data = io_utils.clean_data(data)
        clean_data_df = pd.DataFrame(clean_data)
        #exmpel på hur man kallar fram en variable som liger i self:
        #DataProccesing("data/ecommerce_sales.csv").amount_of_orders_df
        self.clean_data_df = clean_data_df
        
    def key_words(self):
        avo = metrics.average_vaule_order(df=self.clean_data_df)
        revenue = metrics.total_index(df=self.clean_data_df,index="revenue")
        unints =  metrics.total_index(df=self.clean_data_df,index="units")
        orders = metrics.amount_of_orders(df=self.clean_data_df)
    
        
        
        return print(f"Aov: {avo} kr per order. {"\n"}Antalet ordrar: {orders} st. {"\n"}Inkomst: {revenue} kr. {"\n"}Antal enheter: {unints} st.")
        


  
  
        
        
   

    





"""Skapar vi en klass som hämtar värden från metrics.
Klassen ska retunera våra nyckelvärden, förslagvis:
- Antal ordrar
- Total antal enheter
- Medelordervärde (AVO)
- Total intäkt"""