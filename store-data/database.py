import mysql.connector

# Database connection configuration

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "data_storage"
    )
    return conn
