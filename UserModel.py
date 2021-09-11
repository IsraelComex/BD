from datetime import datetime



class UserModel:

    

  def __init__(self, name, email, password, id=None, createAt=None):
    self.__createAt = createAt if createAt else datetime.now()
    self.__email = email
    self.__id = id
    self.__name = name
    self.__password = password

    

  @property
  def createAt(self):
    return self.__createAt
  @createAt.setter
  def createAt(self, createAt):
    self.__createAt = createAt
   

  @property
  def email(self):
    return self.__email
  @email.setter
  def email(self, email):
    self.__email = email
  

  @property
  def id(self):
    return self.__id
  

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, name):
    self.__name = name

  
  @property
  def password(self):
    return self.__password
  @password.setter
  def password(self, password):
    self.__password = password

