from extract import *
from transform import *
from anomaly import *
from load import *
from report import *
from datetime import datetime

if __name__ == "__main__":

    date_debut = "2026-01-01"
    date_fin = datetime.now()
    date_fin = date_fin.strftime("%Y-%m-%d")

    data = extract_data_date(date_debut, date_fin)
    if data:
        df = ordonner_data(data)

        df = clean_data(df)
        df = enrichir_data(df)
        df = detect_anomaly(df)
        
        save_tosqlite(df)
        anomalies_df = check_anomaly_db()
        generate_html(df)
        generate_html_anomalies(anomalies_df)


        
