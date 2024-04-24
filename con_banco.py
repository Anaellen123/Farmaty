import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'G-op198Ana',
    'host': '127.0.0.1',
    'database': 'jogoteca',
    'raise_on_warnings': True


}

#conn = mysql.connector.connect(user = 'root',
 #                              password = 'G-op198Ana',
#                               host = '127.0.0.1',
#                               database = 'jogoteca')


try:
    conn = mysql.connector.connect(
        **config
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Somenthing is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    conn.close()
