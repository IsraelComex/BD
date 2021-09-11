from mysql.connector.errors import Error


class UserDB:

  


  def __init__(self, connection):
    self.connection = connection


   

  def save(self, user):
    try:
      cursor = self.connection.cursor()
      sql = 'insert into users (name, email, password, createAt) values (%s, %s, %s, %s)'
      cursor.execute(sql, (user.name, user.email, user.password, user.createAt))
      self.connection.commit()
    except Error as e:
      return e

