import customtkinter


class familyFrame(customtkinter.CTkFrame):
  def __init__(self, master, fg_color, text_color):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=fg_color)

    self.mainHeading=customtkinter.CTkLabel(self, text='Family Type', font=('Helvetica', 36, 'bold'), text_color=text_color)
    self.mainHeading.place(x=130, y=20)

    self.sedanCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.sedanCardFrame.place(x=130, y=160)

    self.suvCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.suvCardFrame.place(x=500, y=160)