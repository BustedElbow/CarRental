import customtkinter 
from PIL import Image
import main

class loginWindow(customtkinter.CTk):
  def login(self):
    username = self.userEntry.get()
    password = self.passEntry.get()

    if username == 'admin' and password == '123':
      print('Login Successful')
      self.destroy()
      main.mainWindow()
    else:
      print('Login Failed')

  def __init__(self):
    super().__init__()

    mainClr = '#4B9AF6'
    actClr = '#1C3076'

    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 800) // 2  
    y = (screen_height - 450) // 2

    self.geometry(f'800x450+{x}+{y}')
    self.resizable(False, False)
    self.title('RMJ Car Rentals - Login')

    self.winHeading=customtkinter.CTkLabel(self, text='RMJ Car Rentals', font=('Helvetica', 32, 'bold'), text_color=mainClr)
    self.winHeading.place(x=50, y=70)

    self.winSlogan=customtkinter.CTkLabel(self, text='Your journey starts here.', font=('Helvetica', 16, 'bold'), text_color='white')
    self.winSlogan.place(x=50, y=110)
    
    self.image=customtkinter.CTkImage(light_image=Image.open('images/carBlueTop.png'), size=(360,179))
    self.imageLabel=customtkinter.CTkLabel(self, image=self.image, text='')
    self.imageLabel.place(x=40, y=210)


    self.loginFrame=customtkinter.CTkFrame(self, width=320, height=340, fg_color=mainClr,)
    self.loginFrame.place(relx=1, rely=0.5, anchor='e', x=-30)

    self.loginHeading=customtkinter.CTkLabel(self.loginFrame, text='Login into your Account', font=('Helvetica', 18, 'bold'), text_color='black')
    self.loginHeading.place(x=55, y=45)

    self.userLabel=customtkinter.CTkLabel(self.loginFrame, text='Username', font=('Helvetica', 12, 'bold'), text_color='black')
    self.userLabel.place(x=45,y=90)

    self.userEntry=customtkinter.CTkEntry(self.loginFrame, width=240, border_color=mainClr, text_color='black', fg_color='white', corner_radius=16, height=35)
    self.userEntry.place(x=40, y=115)

    self.passLabel=customtkinter.CTkLabel(self.loginFrame, text='Password', font=('Helvetica', 12, 'bold'), text_color='black')
    self.passLabel.place(x=45, y=165)

    self.passEntry=customtkinter.CTkEntry(self.loginFrame, width=240, border_color=mainClr, text_color='black', fg_color='white' ,corner_radius=16, height=35, show='*',)
    self.passEntry.place(x=40, y=190)

    self.loginBtn=customtkinter.CTkButton(self.loginFrame, command=self.login, text='Login', font=('Helvetica', 12, 'bold'), fg_color=actClr, text_color='white', width=110, height=40, corner_radius=20)
    self.loginBtn.place(x=43, y=250)

    self.signBtn=customtkinter.CTkButton(self.loginFrame, text='Sign Up', font=('Helvetica', 12, 'bold'), fg_color='white',text_color='black', width=110, height=40, corner_radius=20)
    self.signBtn.place(x=168, y=250)

    self.mainloop()


loginWindow()