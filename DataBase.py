import mysql.connector
from mysql.connector import Error



class DataBase:
 

  def __init__(self):
    pass


  def connect(self):
    try:
      con = mysql.connector.connect(
        host="localhost", 
        database="db_user_app", 
        user="root", 
        password="aluno99"
      )
      if con.is_connected():
        return con, True
    except Error as e:
      return e, False