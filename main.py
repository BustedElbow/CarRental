import customtkinter

class mainWindow(customtkinter.CTk):

  def showFamPage(self):
    self.famFrame.tkraise()



  def __init__(self):
    super().__init__()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 1600) // 2  
    y = (screen_height - 900) // 2
    self._set_appearance_mode('dark')

    mainClr = '#4B9AF6'
    actClr = '#1C3076'
    frameClr = '#242424'

    self.geometry(f'1600x900+{x}+{y}')
   
    self.title('RMJ Car Rentals')

    self.sideFrame=customtkinter.CTkFrame(self, width=150, height=900, fg_color=mainClr, corner_radius=0) 
    self.sideFrame.place(relx=0, rely=0.5, anchor='w')


    self.clsfMainFrame=customtkinter.CTkFrame(self, width=1450, height=900, corner_radius=0, fg_color=frameClr)
    self.clsfMainFrame.place(relx=1, rely=0.5, anchor='e')


    self.famFrame=customtkinter.CTkFrame(self, width=1450, height=900, corner_radius=0, fg_color=frameClr)
    self.famFrame.place(relx=1, rely=0.5, anchor='e')


    self.famLabel=customtkinter.CTkLabel(self.famFrame, text='Family Type', font=('Helvetica', 32, 'bold'), text_color=mainClr)
    self.famLabel.place(x=300, y=20)


    self.classlabel=customtkinter.CTkLabel(self.clsfMainFrame, text='Vehicle Classification', font=('Helvetica', 32, 'bold'), text_color=mainClr)
    self.classlabel.place(x=300, y=20)


    # Family Frame
    self.famCardFrame=customtkinter.CTkFrame(self.clsfMainFrame, width=350, height=600, fg_color='white')
    self.famCardFrame.place(x=300, y=160)

    self.famBtn=customtkinter.CTkButton(self.famCardFrame, command=self.showFamPage,text='View', fg_color=mainClr)
    self.famBtn.place(x=100, y=10)

    # # Vacation Frame
    # self.vacFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white')
    # self.vacFrame.place(x=700, y=160)

    # self.vacBtn=customtkinter.CTkButton(self.vacFrame, text='View', fg_color=mainClr)
    # self.vacBtn.place(x=100, y=10)

    # # Mover Frame
    # self.movFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white')
    # self.movFrame.place(x=1100, y=160)

    # self.movBtn=customtkinter.CTkButton(self.movFrame, text='View', fg_color=mainClr)
    # self.movBtn.place(x=100, y=10)


    self.clsfMainFrame.tkraise()

    self.mainloop()


mainWindow()