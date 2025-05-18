import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SamSQL!00",
    database="Crypto_prices"
)

query = "SELECT * FROM crypto_prices"
df = pd.read_sql(query, connection)
print(df)

connection.close()
