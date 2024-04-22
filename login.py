import customtkinter 

class UserLoginFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    
    windowBgClr = self.cget('background')

    self.userLabel = customtkinter.CTkLabel(
      self, 
      text='Username', 
      bg_color=windowBgClr, 
      text_color='black'
      )

    self.userEntry = customtkinter.CTkEntry(
      self, 
      bg_color=windowBgClr, 
      fg_color=windowBgClr
      )
    self.userEntry.pack()

    self.loginBtn = customtkinter.CTkButton(
      self, 
      text='login', 
      corner_radius=16,
      fg_color='#65AFFF', 
      bg_color=windowBgClr)
    self.loginBtn.pack(pady=20)

    self.mainloop()
    self.userLabel.pack()


class LoginWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.title('Login')
    self.geometry('700x500')
    self._set_appearance_mode('light')



LoginWindow()