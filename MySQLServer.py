#MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
    # Execute SQL statements using the execute() method on the cursor
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        # handles any error that occurs during connection
        print(f"Error")

    finally:
        # Close connection to the databasse
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")
