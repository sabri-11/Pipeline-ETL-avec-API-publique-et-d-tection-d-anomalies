from extract import *
from transform import *
from anomaly import *


if __name__ == "__main__":

    data = extract_data_date("2026-01-01", "2026-05-03")
    if data:
        df = ordonner_data(data)

        df = clean_data(df)
        df = enrichir_data(df)
        df = detect_anomaly(df)
        
