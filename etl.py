import requests
import pandas as pd
import sqlite3


def extract() -> dict:
    """ API for extracting data from
    https://api.nbp.pl/
    """

    # A series of the last 100 quotations of the average EUR exchange rate in JSON format
    API_URL = "https://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json"
    data = requests.get(API_URL).json()
    return data


def transform(data: dict) -> pd.DataFrame:
    """ Transformation of the dataset - average of the last 100 EUR exchange rate quotations based on NBP data  """
    df = pd.DataFrame(data["rates"])
    print(f"Number of average EUR quotations   {len(df)}")
    df = df[df["mid"] >= 4.50]
    print(f"Number of EUR exchange rates above 4,50 of the last 100 quotations {len(df)}")
    return df[["effectiveDate", "mid"]]


def load(df: pd.DataFrame) -> None:
    """ Loading data into sqlite database"""
    try:
        conn = sqlite3.connect('EUR_exchange_rate.db')
        df.to_sql('EUR_T', conn, if_exists='replace', index=False)

    except sqlite3.Error as err:
        print("Connection error", err)
    finally:
        conn.close()

