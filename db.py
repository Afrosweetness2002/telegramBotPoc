from typing import Final
import os;
import mysql.connector
from mysql.connector import errorcode

MYSQL_USERNAME: Final = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD: Final = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST: Final = os.getenv("MYSQL_HOST")
MYSQL_PORT: Final = os.getenv("MYSQL_PORT")

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
def connect():
    try:
        cnx = mysql.connector.connect(
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database='quran_class')

        with cnx.cursor() as cursor:

            result = cursor.execute("SELECT * FROM role")

            rows = cursor.fetchall()

            for rows in rows:
                print(rows)

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password.")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()