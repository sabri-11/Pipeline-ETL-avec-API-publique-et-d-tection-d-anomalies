import pandas as pd

def detect_anomaly(df, columns="usd_pct_change"):
 
    q1 = df[columns].quantile(0.25)
    q3 = df[columns].quantile(0.75)

    iqr = q3 - q1 

    lower_bound = q1 - 1.5*iqr
    upper_bound = q3 + 1.5*iqr

    df["is_anomaly"] = (df[columns] < lower_bound) | (df[columns] > upper_bound) # | = or pour une série binaire
    

    df["explication"] = df[columns].apply(get_reason, args=(lower_bound, upper_bound))

    # print(df[df["is_anomaly"]==True])  # affiche uniquement les valeures anormales 

    return df


def get_reason(arg, lb, ub): 
    if arg < lb:
        return "Inférieure référence"
    elif arg > ub:
        return "Supérieure référence"
    else: 
        return "RAS"