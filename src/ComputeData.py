#vill att göra: ta sök ord och retunera intäker bonus mål att return top lista.

import csv

class ReveuneAnylist:
    def __init__(self,file):
        with open(file,"r",encoding="utf-8") as file:
            dict_reader = csv.DictReader(file)
            contents = []
            for row in dict_reader:
                contents.append(row)
            self.dict_contents_list = contents
    
    
   
    


#print(ReveuneAnylist("data/ecommerce_sales.csv").dict_contents_list)