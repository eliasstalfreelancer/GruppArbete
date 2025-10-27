
"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""
import io_utils
import pandas as pd
import ecommerce

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
        revenue = ecommerce.totel_index_from_difrent_cuntries(df=self.clean_data_df,index="revenue")
        unints =  ecommerce.totel_index_from_difrent_cuntries(df=self.clean_data_df,index="units")
        orders = ecommerce.amount_of_orders(df=self.clean_data_df)
    
        
        result = orders
        result["unints"] = unints
        result["revenue"] = revenue
        result["avo"] = avo
        return result


print(DataProccesing("data/ecommerce_sales.csv").key_words())

"""Här vill vi smala alla uträkningar som vi ska använda för att sedan skapa diagram i viz.py"""

