SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS python_connection;
USE python_connection;


CREATE TABLE users(
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL
);

SHOW TABLES; 


