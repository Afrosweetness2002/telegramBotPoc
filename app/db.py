from typing import Final
import os
import mysql.connector
from mysql.connector import errorcode

MYSQL_USERNAME: Final = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD: Final = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST: Final = os.getenv("MYSQL_HOST")
MYSQL_PORT: Final = os.getenv("MYSQL_PORT")

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
def get(query: str):
    try:
        cnx = mysql.connector.connect(
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database='quran_class')
        
        try:
          with cnx.cursor() as cursor:
              result = cursor.execute(query)
              all = cursor.fetchall()
              print(f"Executed query: {query}")
              print(all)
              return all

        except Exception as ex:
          print(ex)

        finally:
          cnx.close()

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("db error: Invalid username or password.")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("db error: Database does not exist")
      else:
        print(err)
  
    except Exception as ex:
      print(ex)