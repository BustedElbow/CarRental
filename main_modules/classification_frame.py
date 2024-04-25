import customtkinter

class classificationFrame(customtkinter.CTkFrame):
  def showFamPage(self):
    self.familyFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, family_frame):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.classlabel=customtkinter.CTkLabel(self, text='Vehicle Classification', font=('Helvetica', 32, 'bold'), text_color=mainClr)
    self.classlabel.place(x=300, y=20)

    self.familyFrame=family_frame

    #  Family Frame
    self.famCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white')
    self.famCardFrame.place(x=300, y=160)

    self.famBtn=customtkinter.CTkButton(self.famCardFrame, command=self.showFamPage,text='View', fg_color=mainClr)
    self.famBtn.place(x=100, y=10)

    # # Vacation Frame
    self.vacFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white')
    self.vacFrame.place(x=700, y=160)

    self.vacBtn=customtkinter.CTkButton(self.vacFrame, text='View', fg_color=mainClr)
    self.vacBtn.place(x=100, y=10)

    # # Mover Frame
    self.movFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white')
    self.movFrame.place(x=1100, y=160)

    self.movBtn=customtkinter.CTkButton(self.movFrame, text='View', fg_color=mainClr)
    self.movBtn.place(x=100, y=10)
