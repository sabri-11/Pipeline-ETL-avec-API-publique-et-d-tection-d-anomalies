import requests
import pandas as pd

def extract_data_date(date_debut, date_fin, base="EUR", target="USD,GBP"):
    url = f"https://api.frankfurter.app/{date_debut}..{date_fin}"

    params = {
        "from": base,
        "to": target
    }

    try:
        rep = requests.get(url, params=params)

        rep.raise_for_status()

        data = rep.json()
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur d'appel API : {e}")
        return None
    
def ordonner_data(data):
    df = pd.DataFrame.from_dict(data['rates'], orient="index")
    df = df.reset_index().rename(columns={"index":"date"})

    return df



    
