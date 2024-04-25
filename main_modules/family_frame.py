import customtkinter


class familyFrame(customtkinter.CTkFrame):
  def __init__(self, master, fg_color, text_color):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=fg_color)

    self.mainHeading=customtkinter.CTkLabel(self, text='Family Type', font=('Helvetica', 32, 'bold'), text_color=text_color)
    self.mainHeading.place(x=300, y=20)