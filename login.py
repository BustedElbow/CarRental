import customtkinter 
from PIL import Image
import os
import main

class loginWindow(customtkinter.CTk):
  def login(self):
    username = self.user_entry.get()
    password = self.pass_entry.get()

    if username == 'admin' and password == '123':
      print('Login Successful')
      self.destroy()
      main.mainWindow()
    else:
      print('Login Failed')

  def __init__(self):
    super().__init__(fg_color='#242424')

    main_color = '#4B9AF6'
    sec_color = '#1C3076'

    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 800) // 2  
    y = (screen_height - 450) // 2
    
    self._set_appearance_mode('dark')
    self.geometry(f'800x450+{x}+{y}')
    self.resizable(False, False)
    self.title('RMJ Car Rentals - Login')

    self.win_heading=customtkinter.CTkLabel(self, text='RMJ Car Rentals', font=('Helvetica', 32, 'bold'), text_color=main_color)
    self.win_heading.place(x=50, y=70)

    self.win_slogan=customtkinter.CTkLabel(self, text='Your journey starts here.', font=('Helvetica', 16, 'bold'), text_color='white')
    self.win_slogan.place(x=50, y=110)
    
    # Image initialization
    self.main_dir=os.path.dirname(os.path.realpath(__file__))
    self.folder_path=os.path.join(self.main_dir, 'images')
    self.logo_path=os.path.join(self.folder_path, 'carBlueTop.png')

    self.image=customtkinter.CTkImage(light_image=Image.open(self.logo_path), size=(360,179))
    self.image_label=customtkinter.CTkLabel(self, image=self.image, text='')
    self.image_label.place(x=40, y=210)

    self.login_frame=customtkinter.CTkFrame(self, width=320, height=340, fg_color=main_color,)
    self.login_frame.place(relx=1, rely=0.5, anchor='e', x=-30)

    self.login_heading=customtkinter.CTkLabel(self.login_frame, text='Login into your Account', font=('Helvetica', 18, 'bold'), text_color='black')
    self.login_heading.place(x=55, y=45)

    self.user_label=customtkinter.CTkLabel(self.login_frame, text='Username', font=('Helvetica', 12, 'bold'), text_color='black')
    self.user_label.place(x=45,y=90)

    self.user_entry=customtkinter.CTkEntry(self.login_frame, width=240, border_color=main_color, text_color='black', fg_color='white', corner_radius=16, height=35)
    self.user_entry.place(x=40, y=115)

    self.pass_label=customtkinter.CTkLabel(self.login_frame, text='Password', font=('Helvetica', 12, 'bold'), text_color='black')
    self.pass_label.place(x=45, y=165)

    self.pass_entry=customtkinter.CTkEntry(self.login_frame, width=240, border_color=main_color, text_color='black', fg_color='white' ,corner_radius=16, height=35, show='*',)
    self.pass_entry.place(x=40, y=190)

    self.login_btn=customtkinter.CTkButton(self.login_frame, command=self.login, text='Login', font=('Helvetica', 12, 'bold'), fg_color=sec_color, text_color='white', width=110, height=40, corner_radius=20)
    self.login_btn.place(x=100, y=250)

    # self.sign_btn=customtkinter.CTkButton(self.login_frame, text='Sign Up', font=('Helvetica', 12, 'bold'), fg_color='white',text_color='black', width=110, height=40, corner_radius=20)
    # self.sign_btn.place(x=168, y=250)

    self.mainloop()
  

loginWindow()