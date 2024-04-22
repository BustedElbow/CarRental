import customtkinter 

class UserLoginFrame(customtkinter.CTkFrame):
  def __init__(self, master, fg_color, bg_color):
    super().__init__(master, fg_color=fg_color, bg_color=bg_color)
   
    self.userLabel = customtkinter.CTkLabel(
      self, 
      text='Username', 
      bg_color=fg_color,
      text_color='white',
      anchor='w'
      )
    self.userLabel.pack(pady=(10, 0), padx=(12, 0) , fill='x')

    self.userEntry = customtkinter.CTkEntry(
      self, 
      bg_color=fg_color,
      fg_color='white',
      text_color='black'
      )
    self.userEntry.pack(padx=10)

    self.passLabel = customtkinter.CTkLabel(
      self,
      text='Password',
      bg_color=fg_color,
      text_color='white',
      anchor='w'
    )
    self.passLabel.pack(pady=(10, 0), padx=(12,0), fill='x')

    self.passEntry = customtkinter.CTkEntry(
      self,
      bg_color=fg_color,
      fg_color='white',
      text_color='black',
      show='*'
    )
    self.passEntry.pack()

    self.loginBtn = customtkinter.CTkButton(
      self, 
      text='login', 
      corner_radius=8,
      fg_color='#65AFFF', 
      bg_color=fg_color,
    )
    self.loginBtn.pack(pady=(10, 20), padx=10)



class LoginWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.title('Login')
    self.geometry('700x500')
    self._set_appearance_mode('light')

    windowBgClr = self.cget('background')
    self.Uframe = UserLoginFrame(
      master=self, 
      bg_color=windowBgClr, 
      fg_color='#1B2845',
      )
    self.Uframe.place(relx=1, rely=0.5, anchor='e', x=1)

    self.mainloop()


LoginWindow()