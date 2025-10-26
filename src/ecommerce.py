"""Läs in funktioner från metrics"""


import io_utils
import pandas as pd

class DataProccesing:
    def __init__(self,path):
        data = io_utils.load_data(path)
        clean_data = io_utils.clean_data(data)
        clean_data_df = pd.DataFrame(clean_data)
        
        amount_of_orders = clean_data_df.groupby("city",observed=False)["revenue"].count()
        amount_of_orders_df = pd.DataFrame(amount_of_orders)
        amount_of_orders_df = amount_of_orders_df.rename(columns={"revenue": "Amount of orders"})

        #exmpel på hur man kallar fram en variable som liger i self:
        #DataProccesing("data/ecommerce_sales.csv").amount_of_orders_df
        #Output: 2500
        self.amount_of_orders_df = amount_of_orders_df
        self.clean_data_df = clean_data_df
        

    #används för att få ut summan av enheter och intäkt
    def totel_index_from_difrent_cuntries(self,index):
        clean_data_df = self.clean_data_df
        sum = clean_data_df.groupby("city").agg(index_sum = (index,"sum")).sort_values("index_sum",ascending=False)
        
        return sum

    def avo(self):
        
        clean_data_df = self.clean_data_df
        
        avo = clean_data_df.groupby("city",observed=False)["revenue"].mean()
        avo_df = pd.DataFrame(avo)
        avo_df = avo_df.round(2)
        avo_df = avo_df.rename(columns={"revenue": "AVO"})
        
        
        return avo_df
    


    
def key_words():
    avo = DataProccesing("data/ecommerce_sales.csv").avo()
    revenue = DataProccesing("data/ecommerce_sales.csv").totel_index_from_difrent_cuntries("revenue")
    unints = DataProccesing("data/ecommerce_sales.csv").totel_index_from_difrent_cuntries("units")
    orders = DataProccesing("data/ecommerce_sales.csv").amount_of_orders_df
    
    
    result = orders
    result["unints"] = unints
    result["revenue"] = revenue
    result["avo"] = avo
    return result




"""Skapar vi en klass som hämtar värden från metrics.
Klassen ska retunera våra nyckelvärden, förslagvis:
- Antal ordrar
- Total antal enheter
- Medelordervärde (AVO)
- Total intäkt"""