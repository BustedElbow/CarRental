import customtkinter

class vacationFrame(customtkinter.CTkFrame):
  def previousFrame(self):
    a = 1

  def __init__(self, master, mainClr, frameClr):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.mainHeading=customtkinter.CTkLabel(self, text='Vehicle List', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)

    self.canvas=customtkinter.CTkCanvas(self, bg=frameClr, width=1450, height=815, highlightthickness=0, scrollregion=(0, 0, 0, 1500))
    self.canvas.place(x=1, y=85)