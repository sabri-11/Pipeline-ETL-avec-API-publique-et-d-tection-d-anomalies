import sqlite3
import pandas as pd
import os


def save_tosqlite(df, table_name="exchange_rates", db_name="../bdd/database.db"):

    dossier = os.path.dirname(db_name)
    if dossier: 
        os.makedirs(dossier, exist_ok=True)

    conn = sqlite3.connect(db_name)

    try:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Données de la table {table_name} chargées dans sqlite\n")

    finally: 
        conn.close()
    

def check_anomaly_db(db_name="../bdd/database.db"):

    conn = sqlite3.connect(db_name)

    query = "SELECT * FROM exchange_rates WHERE is_anomaly = 1"

    anomalies_df = pd.read_sql_query(query, conn)
    conn.close()

    # print(f"{len(anomalies_df)} anomalies détectées : \n {anomalies_df}")

    return anomalies_df