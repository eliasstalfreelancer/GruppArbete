"""läs in funktioner från metrics"""
import matplotlib.pyplot as plt
import pandas as pd
from src.metrics import order_per_month, order_per_weekday
import matplotlib.pyplot as plt
import pandas as pd


def plot_orders_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Skapar diagram för ordrar per veckodag"""
    order_per_weekday(df).plot.line(x='day_of_week', y='num_order_per_week', marker='o',color='green')
    plt.title('Number of Orders per Weekday')
    return plt.show()


def plot_orders_month(df: pd.DataFrame) -> pd.DataFrame:
    """Skapar diagram för ordrar per månad"""
    order_per_month(df).plot.line(x='month', y='num_orders', marker='o')
    plt.title('Number of Orders per Month')
    return  plt.show()


"""
Skapa olika diagram med värden från metrics
"""
def bar(ax, x, y, title, xlabel, ylabel, grid=True):
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis='y')
    return ax

def box(ax, df, x, y, title, xlabel, ylabel, grid=True):
    df.boxplot(column=x, by=y, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis='y')
    ax.grid(False, axis='x')
    plt.suptitle('')
    return ax