import mysql.connector
conn = mysql.connector.connect(host='localhost',password='EnterYourPassword', user='root')

if conn.is_connected():
    print("MySQL Connector Installed Successfully!")

'''
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='EnterYourPassword'
)

if conn.is_connected():
    print("MySQL Connector Installed Successfully!")

    mysql --version
    python --version
    python -m pip install mysql-connector-python

'''