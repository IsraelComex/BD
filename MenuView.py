from tkinter import *
from user.views.UserFormView import UserFormView







class MenuView:







  def __init__(self, parentWidget=None):

    self.__parentWidget = parentWidget

    self.frame = Frame(self.__parentWidget)

    self.frame.pack()



    self.fonts = {

      "button": ("Calibri", "16"), 

      "title": ("Arial", "24", "bold") 

    }



    frameTitleConfig = { "padx": 10, "pady": 10 }

    self.frameTitle = Frame(self.frame, frameTitleConfig)

    self.frameTitle.pack()



    labelTitleConfig = {

      "font": self.fonts["title"],

      "text": "Cadastro de Usuários"

    }

    self.labelTitle = Label(self.frameTitle, labelTitleConfig)

    self.labelTitle.pack()



    frameBodyConfig = { "padx": 10, "pady": 10, "width": 48 }

    self.frameBody = Frame(self.frame, frameBodyConfig)

    self.frameBody.pack()



    buttonsConfig = { "font": self.fonts["button"], "width": 24 }



    self.buttonNewUser = Button(self.frameBody, buttonsConfig)

    self.buttonNewUser["text"] = "Novo Usuário"

    self.buttonNewUser["command"] = self.showNewUserForm

    self.buttonNewUser.pack()



    self.buttonListUser = Button(self.frameBody, buttonsConfig)

    self.buttonListUser["text"] = "Listar Usuários"

    self.buttonListUser.pack()







  def showNewUserForm(self):

    try:

      del self.userFormView

    except AttributeError:

      pass



    self.userFormView = UserFormView(self.__parentWidget)

