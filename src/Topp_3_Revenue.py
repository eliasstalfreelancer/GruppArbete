import ComputeData

def Topp_Revenue(file,search = "category",toppnumber = 3):
    dict_list = ComputeData.ReveuneAnylist(file).dict_contents_list
    revenue_stream = {}
    for row in dict_list:
        if row [search] in revenue_stream:
            revenue_stream [row[search]] += int(float(row["revenue"]))
        else:
            revenue_stream[row[search]] = int(float(row["revenue"]))
    highest_sum = []
    highest_sum_sorted = sorted(revenue_stream.values(),reverse = True)
   # print(highest_sum_sorted)   
    for revenue in highest_sum_sorted:
        for category in revenue_stream:
            if revenue == revenue_stream[category]: 
                highest_sum.append((category,revenue))
  #  print(highest_sum)
    return highest_sum [0:toppnumber]
               
print(Topp_Revenue("data/ecommerce_sales.csv"))


