import pandas as pd
from datetime import datetime

def clean_data(df): 

    df["date"] = pd.to_datetime(df["date"])
    # print(df.head())

    all_dates = pd.date_range(start=df["date"].min(), end=df["date"].max())

    df = df.set_index("date")
    # print(df.head())

    df = df.reindex(all_dates)
    # print(df.head())

    df = df.reset_index()
    # print(df.head())

    df = df.rename(columns={"index":"date"})
    # print(df.head())

    # remplir les Nan par les dernières valeures connues : 
    df = df.ffill()
    # print(df.head())

    return df


def enrichir_data(df): 
    df["usd_pct_change"] = round(df["USD"].pct_change() * 100, 2)
    # print(df.head())
    return df


