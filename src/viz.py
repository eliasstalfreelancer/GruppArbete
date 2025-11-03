"""läs in funktioner från metrics"""
import matplotlib.pyplot as plt
import pandas as pd
import src.metrics as me 

def distro_of_rev(df):   
    # histogram of revenue
    plt.figure(figsize=(10, 6))
    plt.hist(df['revenue'], bins=30, color='salmon', edgecolor='black')
    plt.xlabel('Revenue')
    plt.ylabel('Orders')
    plt.title('Distribution of Revenue')
    plt.grid(True,axis='y')
    plt.show()

def plot_city_revenue(df):
    city_revenue_result = me.city_revenue(df)
    city_revenue_result.plot(
        kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], figsize=(10, 6))
    plt.xlabel('City')
    plt.ylabel('Total Revenue (million)')
    plt.title('Total Revenue by City')
    plt.xticks(rotation=45)
    plt.grid(True,axis='y')
    plt.show()

def plot_orders_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Skapar diagram för ordrar per veckodag"""
    me.order_per_weekday(df).plot.line(x='day_of_week', y='num_order_per_week', marker='o',color='green',label = "Number of orders per week" )
    plt.title('Number of Orders per Weekday')
    plt.xlabel("Day of week")
    plt.ylabel("Orders")
    plt.legend()
    plt.grid(True)
    return plt.show()


def plot_orders_month(df: pd.DataFrame) -> pd.DataFrame:
    """Skapar diagram för ordrar per månad"""
    me.order_per_month(df).plot.line(x='month', y='num_orders', marker='o',label = "Number of orders per Months")
    plt.title('Number of Orders per Month')
    plt.xlabel("Months")
    plt.ylabel("Orders")
    plt.legend()
    plt.grid(True)
    return  plt.show()



#Funktion för bar och box diagram

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
