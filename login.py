import customtkinter 


def login():
  customtkinter.set_appearance_mode('light')

  app=customtkinter.CTk()
  app.geometry('800x450')
  app.resizable(False, False)
  app.title('Login')
  
  mainClr = '#1F487E'
  actClr = '#E94C55'
  
  loginFrame=customtkinter.CTkFrame(master=app, width=320, height=340, fg_color=mainClr, corner_radius=16)
  loginFrame.place(relx=1, rely=0.5, anchor='e', x=-30)
  
  loginHeading=customtkinter.CTkLabel(master=loginFrame, text='Login into your Account', font=('Helvetica', 16, 'bold'), text_color='white')
  loginHeading.place(x=70, y=45)
  
  userLabel=customtkinter.CTkLabel(master=loginFrame, text='Username', font=('Helvetica', 12, 'bold'), text_color='white')
  userLabel.place(x=45,y=90)
  
  userEntry=customtkinter.CTkEntry(master=loginFrame, width=240, border_color=mainClr, text_color='black', corner_radius=8, height=35)
  userEntry.place(x=40, y=115)
  
  passLabel=customtkinter.CTkLabel(master=loginFrame, text='Password', font=('Helvetica', 12, 'bold'), text_color='white')
  passLabel.place(x=45, y=165)
  
  passEntry=customtkinter.CTkEntry(master=loginFrame, width=240, border_color=mainClr, text_color='black', corner_radius=8, height=35, show='*')
  passEntry.place(x=40, y=190)
  
  loginBtn=customtkinter.CTkButton(master=loginFrame, text='Login', font=('Helvetica', 12, 'bold'), fg_color=actClr, text_color='white', width=110)
  loginBtn.place(x=43, y=250)
  
  signBtn=customtkinter.CTkButton(master=loginFrame, text='Sign Up', font=('Helvetica', 12, 'bold'), fg_color='white',text_color='black', width=110)
  signBtn.place(x=168, y=250)
  
  
  app.mainloop()


