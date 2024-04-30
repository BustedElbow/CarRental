import customtkinter

def rentCar(carData):
  return carData

class orderFrame(customtkinter.CTkFrame):
  def updateCarModel(self, model, manufacturer):
    self.cartest.configure(text=f'Selected Car: {manufacturer} {model}')

  def showPreviousFrame(self):
    self.previousFrame.tkraise()

  def __init__(self, master, frameClr, mainClr, previousFrame):
    super().__init__(master, width=1450, height=900, fg_color=frameClr)

    self.previousFrame=previousFrame

    self.mainHeading=customtkinter.CTkLabel(self, text='Ordering Information', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)

    self.backBtn=customtkinter.CTkButton(self, text='Back', font=('Helvetica', 16, 'bold'), command=self.showPreviousFrame, width=50, height=50, corner_radius=50 // 2, fg_color=mainClr)
    self.backBtn.place(x=20, y=20)

    self.mainFrame=customtkinter.CTkFrame(self, width=500, height=500, corner_radius=16, fg_color='white')
    self.mainFrame.place(x=200, y=200)

    self.cartest=customtkinter.CTkLabel(self.mainFrame, text='', font=('Helvetica', 16, 'bold'), text_color='black')
    self.cartest.place(x=50, y=50)
