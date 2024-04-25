import customtkinter

class classificationFrame(customtkinter.CTkFrame):
  def showFamPage(self):
    self.familyFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, family_frame):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.classlabel=customtkinter.CTkLabel(self, text='Vehicle Classification', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.classlabel.place(x=130, y=20)

    self.familyFrame=family_frame

    #  Family Frame
    self.famCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.famCardFrame.place(x=130, y=160)

    self.famImgCon=customtkinter.CTkFrame(self.famCardFrame, width=280, height=280, fg_color='gray', corner_radius=16)
    self.famImgCon.place(x=35, y=30)

    self.famLabel=customtkinter.CTkLabel(self.famCardFrame, text='Family', font=('Helvetica', 32, 'bold'), text_color='black')
    self.famLabel.place(x=125, y=325)

    self.famBtn=customtkinter.CTkButton(self.famCardFrame, command=self.showFamPage, font=('Helvetica', 24, 'bold'), text='View', text_color='black', width=200, height=50, fg_color=mainClr, corner_radius=16)
    self.famBtn.place(x=75, y=520)


    # # Vacation Frame
    self.vacFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.vacFrame.place(x=565, y=160)

    self.vacImgCon=customtkinter.CTkFrame(self.vacFrame, width=280, height=280, fg_color='gray', corner_radius=16)
    self.vacImgCon.place(x=35, y=30)

    self.vacLabel=customtkinter.CTkLabel(self.vacFrame, text='Vacation', font=('Helvetica', 32, 'bold'), text_color='black')
    self.vacLabel.place(x=110, y=325)

    self.vacBtn=customtkinter.CTkButton(self.vacFrame, text='View', width=200, height=50, fg_color=mainClr, font=('Helvetica', 24, 'bold'), corner_radius=16, text_color='black')
    self.vacBtn.place(x=75, y=520)

    # # Mover Frame
    self.movFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.movFrame.place(x=1000, y=160)

    self.movImgCon=customtkinter.CTkFrame(self.movFrame, width=280, height=280, fg_color='gray', corner_radius=16)
    self.movImgCon.place(x=35, y=30)

    self.movLabel=customtkinter.CTkLabel(self.movFrame, text='Mover', font=('Helvetica', 32, 'bold'), text_color='black')
    self.movLabel.place(x=125, y=325)

    self.movBtn=customtkinter.CTkButton(self.movFrame, text='View', width=200, height=50, fg_color=mainClr, font=('Helvetica', 24, 'bold'), corner_radius=16, text_color='black')
    self.movBtn.place(x=75, y=520)
