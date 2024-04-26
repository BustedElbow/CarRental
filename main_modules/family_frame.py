import customtkinter


class familyFrame(customtkinter.CTkFrame):
  def __init__(self, master, mainClr, frameClr):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.mainHeading=customtkinter.CTkLabel(self, text='Family Type', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)


    # Sedan Card Frame
    self.sedanCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.sedanCardFrame.place(x=350, y=160)

    self.sedanLabel=customtkinter.CTkLabel(self.sedanCardFrame, text='Sedan')
    self.sedanLabel.place()

    self.sedanBtn=customtkinter.CTkButton(self.sedanCardFrame, text='View', font=('Helvetica', 24, 'bold'), corner_radius=16, width=200, height=50, text_color='black', fg_color=mainClr)
    self.sedanBtn.place(x=75, y=520)

    # SUV Card Frame
    self.suvCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.suvCardFrame.place(x=750, y=160)

    self.suvLabel=customtkinter.CTkLabel(self.suvCardFrame, text='suv')
    self.suvLabel.place()

    self.suvBtn=customtkinter.CTkButton(self.suvCardFrame, text='View', font=('Helvetica', 24, 'bold'), corner_radius=16, width=200, height=50, text_color='black', fg_color=mainClr)
    self.suvBtn.place(x=75, y=520)