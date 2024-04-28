import customtkinter

class vacationFrame(customtkinter.CTkFrame):
  def showPreviousFrame(self):
    self.previousFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, previousFrame):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.previousFrame=previousFrame

    self.mainHeading=customtkinter.CTkLabel(self, text='Vehicle List', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)

    self.backBtn=customtkinter.CTkButton(self, text='Back', font=('Helvetica', 16, 'bold'), command=self.showPreviousFrame, width=50, height=50, corner_radius=50 // 2)
    self.backBtn.place(x=20, y=20)

    self.canvas=customtkinter.CTkCanvas(self, bg=frameClr, width=1450, height=815, highlightthickness=0, scrollregion=(0, 0, 0, 1500))
    self.canvas.place(x=1, y=85)

    self.carFrame=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.carFrame.place(x=130, y=75)

    self.carFrame2=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.carFrame2.place(x=565, y=75)

    self.carFrame3=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.carFrame3.place(x=1000, y=75)