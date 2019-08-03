import mysql.connector

cnx = mysql.connector.connect(
    user='user',
    password='password',
    host='127.0.0.1'
)
print(cnx.is_connected())
cnx.close()
