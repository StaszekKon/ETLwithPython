from etl import *


def test_extract():
    extracted_data = extract()
    assert isinstance(extracted_data, dict)
    assert "EUR" in extracted_data["code"]


def test_transform():
    sample_data = {
        "rates": [
            {"effectiveDate": "2023-11-01", "mid": 4.55},
            {"effectiveDate": "2023-11-02", "mid": 4.48},
            {"effectiveDate": "2023-11-02", "mid": 4.38},
            {"effectiveDate": "2023-11-02", "mid": 4.67},

        ]
    }
    transformed_df = transform(sample_data)
    assert isinstance(transformed_df, pd.DataFrame)
    assert len(transformed_df) > 0
    assert all(transformed_df["mid"] >= 4.50)


def test_load():
    sample_data = pd.DataFrame({
        "effectiveDate": ["2022-11-01", "2022-11-02"],
        "mid": [4.57, 4.49]
    })
    load(sample_data)

    # Verify that the table has been saved correctly in the database

    conn = sqlite3.connect('EUR_exchange_rate.db')
    cursor = conn.cursor()
    query = "SELECT * FROM EUR_T"
    loaded_data = cursor.execute(query).fetchall()
    assert len(loaded_data) == len(sample_data)
    assert (loaded_data[0][1] == sample_data["mid"][0])
    conn.close()