import customtkinter

class mainWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 1600) // 2  
    y = (screen_height - 900) // 2
    self._set_appearance_mode('dark')

    mainClr = '#4B9AF6'
    actClr = '#1C3076'

    self.geometry(f'1600x900+{x}+{y}')
   
    self.title('RMJ Car Rentals')

    self.topFrame=customtkinter.CTkFrame(self, width=150, height=900, fg_color=mainClr, corner_radius=0) 
    self.topFrame.place(relx=0, rely=0.5, anchor='w')

    self.classlabel=customtkinter.CTkLabel(self, text='Vehicle Classification', font=('Helvetica', 32, 'bold'), text_color=mainClr)
    self.classlabel.place(x=300, y=20)

    self.famFrame=customtkinter.CTkFrame(self, width=350, height=600)
    self.famFrame.place(x=300, y=160)

    self.vacFrame=customtkinter.CTkFrame(self, width=350, height=600)
    self.vacFrame.place(x=690, y=160)

    # self.movFrame=customtkinter.CTkFrame(self, width=350, height=600)





    self.mainloop()


mainWindow()