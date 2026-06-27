CREATE DATABASE data_storage;




USE data_storage;




CREATE TABLE users(

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(50),

surname VARCHAR(50),

email VARCHAR(100),

mobile VARCHAR(15),

age INT,

gender VARCHAR(10)

);