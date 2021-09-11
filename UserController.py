from typing import List
from user.UserModel import UserModel
from DataBase import DataBase
from user.UserDB import UserDB



class UserController:



  def __init__(self):
    db = DataBase()
    connection, connected = db.connect()
    if connected:
      self.__userDB = UserDB(connection)
    else:
      print(f"Erro ao connectar com o banco: {connection}")    



  def save(self, user):
    user = UserModel(
      user['name'], 
      user['email'], 
      user['password'],
      user['id']
    )
    self.__userDB.save(user)

    


  def list(self) -> List:
        users = list()
        for user in self.__userDB.list():
          user_dict = {
            "id": user.id,
            "name": user.name,
            "email": user.email,            
            
          }
               
               
               
     return self.__userDB.list()

