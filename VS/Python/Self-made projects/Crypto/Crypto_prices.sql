CREATE DATABASE crypto_prices;

USE crypto_prices;

CREATE TABLE crypto_prices (
	id INT AUTO_INCREMENT PRIMARY KEY,
    coin_name VARCHAR(50),
    price_usd FLOAT,
    timestamp DATETIME
);