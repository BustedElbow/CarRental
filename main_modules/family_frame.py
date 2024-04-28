import customtkinter


class familyFrame(customtkinter.CTkFrame):
  def showPreviousFrame(self):
    self.previousFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, previousFrame):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.previousFrame=previousFrame

    self.mainHeading=customtkinter.CTkLabel(self, text='Vehicle Type', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)

    self.backBtn=customtkinter.CTkButton(self, text='Back', font=('Helvetica', 16, 'bold'), command=self.showPreviousFrame, width=50, height=50, corner_radius=50 // 2)
    self.backBtn.place(x=20, y=20)