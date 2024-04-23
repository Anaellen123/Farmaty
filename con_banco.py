import mysql.connector

conn = mysql.connector.connect(user = 'root',
                               password = 'G-op198Ana',
                               host = '127.0.0.1',
                               database = 'jogoteca')
conn.close()