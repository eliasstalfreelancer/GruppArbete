
import pandas as pd

"""Här samlar vi alla utsräkningar vi behöver till vår klass i ecommerce.py som presenterar nyckeltal"""




def amount_of_orders(df):
    
    amount_of_orders = len(df) 

    return amount_of_orders


def total_index(df,index):
    #räknar ut summan av valfri cloum
    sum = df[index].sum()
    rounded_sum = sum.round(2)
        
    return rounded_sum

def average_vaule_order(df):
    revenue = total_index(df,"revenue")
    orders = amount_of_orders(df)
    aov = revenue/orders
    rounded_aov = aov.round(2)
    
    return rounded_aov  


def order_per_month(df: pd.DataFrame) -> pd.DataFrame:
    """Räknar unika ordrar per månad"""
    return df.groupby(df['month'])['order_id'].nunique().reset_index(name='num_orders') 


def order_per_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Räknar unika ordrar per veckodag"""
    # rad 40 till 41 är taget från Stack Overflow https://stackoverflow.com/questions/53189216/sorting-pandas-dataframe-by-weekdays?
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return df.groupby(df['day_of_week'])['order_id'].nunique().reset_index(name='num_order_per_week').sort_values(by='day_of_week', key=lambda x: x.map({day: i for i, day in enumerate(week_days)}))




def city_revenue(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("city",observed=False)["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def groupby_category(df):
    """
    Gruperar per categori och räknar: antal, medelvärde och summa för 'revenue' i varje grupp
    """    
    return (
        df.groupby('category', observed=False)['revenue']
        .agg(antal='count', medel='mean', total='sum', std= 'std')
        .sort_values(by='total', ascending=False)
        .reset_index()
        ) 
