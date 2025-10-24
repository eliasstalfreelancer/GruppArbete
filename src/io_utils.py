""" 
1. Börja med att importera bibliotek pandas

2. Skapa en funktion för att läsa in fil som vi sedan kan använda i Notebooken.
    Funktionen ska: 
    *läsa in filen men filepath som vi skickar med
    *retunera pd.read_csv
    
3. Skapa en funktion som 'städar' filen
    Funktionen ska:
    *Sätta rätt datatyper så vi kan använda kategorierna för olika beräkningar senare
    *Retunera df_clean"""


import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df_clean = df
    df_clean["date"] = pd.to_datetime(df_clean["date"], dayfirst=True, errors="coerce")
    df_clean["city"] = df_clean["city"].astype("category")
    df_clean["category"] = df_clean["category"].astype("category")
    return df_clean