import requests
import pandas as pd
from datetime import datetime
import mysql.connector
from mysql.connector import Error

# Step 1: API Call
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Step 2: Transform into DataFrame
    records = []
    for crypto, price_info in data.items():
        records.append({
            "crypto": crypto,
            "price_usd": price_info["usd"],
            "timestamp": datetime.now()
        })

    df = pd.DataFrame(records)
    print(df)

    # Step 3: Load into MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SamSQL!00",
            database="Crypto_prices"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO crypto_prices (coin_name, price_usd, timestamp)
                VALUES (%s, %s, %s)
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, (row["crypto"], row["price_usd"], row["timestamp"]))

            connection.commit()
            print("✅ Data successfully inserted into MySQL!")

    except Error as e:
        print("❌ Error while connecting to MySQL:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

else:
    print("❌ Failed to fetch data:", response.status_code)
