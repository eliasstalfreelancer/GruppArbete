"""läs in funktioner från metrics"""
from src.metrics import order_per_month, order_per_weekday
import matplotlib.pyplot as plt
import pandas as pd


def plot_orders_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Skapar diagram för ordrar per veckodag"""
    order_per_weekday(df).plot.line(x='day_of_week', y='num_order_per_week', marker='o',color='green')
    return plt.title('Number of Orders per Weekday'), plt.show()


def plot_orders_month(df: pd.DataFrame) -> pd.DataFrame:
    """Skapar diagram för ordrar per månad"""
    order_per_month(df).plot.line(x='month', y='num_orders', marker='o')
    return plt.title('Number of Orders per Month'), plt.show()


"""Skapa olika diagram med värden från metrics

1. Vad säljer vi - vilka kategorier driver mest intäkt
                 - AVO per kategori 
2. Var säljer vi - vilka städer driver mest intäkt
                 - AVO per stad
3. När säljer vi - intäkt per månad?
4. Top 3         - vilka tre kategorier driver mest intäkt"""