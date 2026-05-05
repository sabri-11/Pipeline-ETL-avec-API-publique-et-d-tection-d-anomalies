import pandas as pd
import os

def generate_html(df, filename="../rapport/report.html"): 

    dossier = os.path.dirname(filename)
    if dossier: 
        os.makedirs(dossier, exist_ok=True)
    
    table_html = df.to_html(classes='mystyle', index=False)
    start_date = df["date"].min()
    end_date = df["date"].max()
    total_entries = len(df)
    total_anomalies = df["is_anomaly"].sum()

    html_template = f"""
    <html>
    <head>
        <title>Rapport ETL - Taux de Change</title>
    </head>
    <body>
        <h1>Rapport de Pipeline de Données</h1>

        <p><strong>Période :</strong> du {start_date} au {end_date}</p>
        <p><strong>Total de lignes traitées :</strong> {total_entries}</p>
        <p><strong>Nombre d'anomalies détectées :</strong> {total_anomalies}</p>

        
        <h2>Données détaillées</h2>
        {table_html}
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)


def generate_html_anomalies(anomalies_df, filename="../rapport/anomalies.html"):

    dossier = os.path.dirname(filename)
    if dossier: 
        os.makedirs(dossier, exist_ok=True)

    table_html = anomalies_df.to_html(classes='mystyle', index=False)

    total_anomalies = len(anomalies_df)

    html_template = f"""
    <html>
    <head>
        <title>Rapport Anomalies</title>
    </head>
    <body>
        <h1>Rapport d'anomalies détectées</h1>

        <p><strong>Nombre d'anomalies détectées :</strong> {total_anomalies}</p>

        
        <h2>Données détaillées</h2>
        {table_html}
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)