from tkinter import *
from user.UserController import UserController




class UserFormView:




  def __init__(self, parentWidget, user=None):
    self.user = user
    self.controller = UserController()
    self.__parentWidget = parentWidget
    self.frame = Frame(self.__parentWidget)
    self.frame.pack()



    self.fonts = {
      "button": ("Calibri", "16"),
      "formLabel": ("Arial", "24"),
      "title": ("Arial", "24", "bold") 
    }



    frameTitleConfig = { "padx": 10, "pady": 10 }
    self.frameTitle = Frame(self.frame, frameTitleConfig)
    self.frameTitle.pack()


    labelTitleConfig = {
      "font": self.fonts["title"],
      "text": f"Editar dados de {user.name}" if user else "Criar novo usuário"
    }
    self.labelTitle = Label(self.frameTitle, labelTitleConfig)
    self.labelTitle.pack()



    frameFieldConfig = { "padx": 20 }


    self.frameFieldName = Frame(self.frame, frameFieldConfig)
    self.frameFieldName.pack()
    self.labelFieldName = Label(self.frameFieldName, font = self.fonts["formLabel"], text = "Nome")
    self.labelFieldName.pack(side=TOP)
    self.name = Entry(self.frameFieldName, font = self.fonts["formLabel"], width = 60)
    self.name.pack(side=LEFT)


    self.frameFieldEmail = Frame(self.frame, frameFieldConfig)
    self.frameFieldEmail.pack()
    self.labelFieldEmail = Label(self.frameFieldEmail, font = self.fonts["formLabel"], text = "Email")
    self.labelFieldEmail.pack(side=TOP)
    self.email = Entry(self.frameFieldEmail, font = self.fonts["formLabel"], width = 60)
    self.email.pack(side=LEFT)


    self.frameFieldPassword = Frame(self.frame, frameFieldConfig)
    self.frameFieldPassword.pack()
    self.labelFieldPassword = Label(self.frameFieldPassword, font = self.fonts["formLabel"], text = "Senha")
    self.labelFieldPassword.pack(side=TOP)
    self.password = Entry(self.frameFieldPassword, font = self.fonts["formLabel"], show="*", width = 60)
    self.password.pack(side=LEFT)


    self.frameFooterButtons = Frame(self.frame, pady = 20)
    self.frameFooterButtons.pack()
    buttonsConfig = { "font": self.fonts["button"], "width": 24 }
    self.buttonSave = Button(self.frameFooterButtons, buttonsConfig)
    self.buttonSave["command"] = self.saveUser
    self.buttonSave["text"] = "Salvar"
    self.buttonSave.pack()




  

  def __del__(self):
    for widget in self.frame.winfo_children():
      widget.destroy()

    self.frame.pack_forget()



  

  def saveUser(self):
    user = {
      "id": self.user.id if self.user else None,
      "name": self.name.get(),
      "email": self.email.get(),
      "password": self.password.get()
    }
    self.controller.save(user)