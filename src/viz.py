"""läs in funktioner från metrics"""


"""Skapa olika diagram med värden från metrics

1. Vad säljer vi - vilka kategorier driver mest intäkt
                 - AVO per kategori 
2. Var säljer vi - vilka städer driver mest intäkt
                 - AVO per stad
3. När säljer vi - intäkt per månad?
4. Top 3         - vilka tre kategorier driver mest intäkt"""
import matplotlib.pyplot as plt
import src.metrics as me 

def plot_city_revenue(df):
    city_revenue_result = me.city_revenue(df)
    city_revenue_result.plot(
        kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], figsize=(10, 6))
    plt.xlabel('City')
    plt.ylabel('Total Revenue (million)')
    plt.title('Total Revenue by City')
    plt.xticks(rotation=45)
    plt.show()