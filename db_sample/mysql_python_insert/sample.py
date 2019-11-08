import mysql.connector

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

cnx = mysql.connector.connect(
    user='user',
    password='password',
    host='127.0.0.1'
)
print(cnx.is_connected())
cnx.close()
