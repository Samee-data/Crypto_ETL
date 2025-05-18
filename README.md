Crypto_ETL
Project Overview
Crypto_ETL is a simple project that collects cryptocurrency price data from an API and stores it in a SQL database for easy querying and analysis.

Project Files
Crypto_prices.sql — SQL script to create the database table schema for storing crypto price data.

get_data.py — Python script to fetch cryptocurrency price data from a public API and insert it into the database.

view_data.py — Python script to query and display stored crypto price data from the database.

Requirements
Python 3.x

requests library (for API calls)

A MySQL database setup

mysql-connector-python (or your preferred MySQL Python connector)

How to Use
Set up your MySQL database and run the Crypto_prices.sql script to create the necessary table.

Configure database connection details inside get_data.py and view_data.py.

Run get_data.py to fetch and store crypto prices.

Run view_data.py to read and display the stored data.

bash
Copy
Edit
python get_data.py
python view_data.py
