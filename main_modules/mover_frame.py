import customtkinter
from tkinter import ttk
from PIL import Image
import os

class moverFrame(customtkinter.CTkFrame):
  def showPreviousFrame(self):
    self.previousFrame.tkraise()

  def rentCarCallBack(self, selectedCar):
    self.orderFrame.updateCarModel(selectedCar['model'], selectedCar['manufacturer'])
    self.orderFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, previousFrame, orderFrame, cars):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.orderFrame=orderFrame
    self.mainClr=mainClr

    self.previousFrame=previousFrame
    self.mainHeading=customtkinter.CTkLabel(self, text='Vehicle Type', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)

    self.backBtn=customtkinter.CTkButton(self, text='Back', font=('Helvetica', 16, 'bold'), command=self.showPreviousFrame, width=50, height=50, corner_radius=50 // 2, fg_color=mainClr)
    self.backBtn.place(x=20, y=20)

    self.canvas=customtkinter.CTkCanvas(self, bg=frameClr, width=1450, height=815, highlightthickness=0, scrollregion=(0, 0, 1000, 2780))
    self.canvas.place(x=1, y=85)

    self.scrollbar=ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
    self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    self.canvas.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -60), 'units'))
    self.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -60), 'units'))

    self.canvas.config(yscrollcommand=self.scrollbar.set)

    self.cars = cars

    self.mainDir = os.path.dirname(os.path.realpath(__file__))
    self.folderPath = os.path.join(self.mainDir, '../images/mover')

    self.createFrames()

  def createFrames(self):
    frameWidth = 350
    frameHeight = 600
    framePaddingX = 90
    framePaddingY = 90
    columns = 3

    for i, car in enumerate(self.cars):
      columnIndex = i % columns
      rowIndex = i // columns

      xPosition = 130 + columnIndex * (frameWidth + framePaddingX)
      yPosition = -20 + framePaddingY + rowIndex * (frameHeight + framePaddingY)

      carFrame = customtkinter.CTkFrame(self.canvas, fg_color='white', width=frameWidth, height=frameHeight, corner_radius=16)
      self.canvas.create_window((xPosition, yPosition), window=carFrame, anchor='nw')

      carImagePath = os.path.join(self.folderPath, f'{car["manufacturer"].lower()}{car["model"].replace(' ', '_').lower()}.jpg')
      carImg = customtkinter.CTkImage(light_image=Image.open(carImagePath), size=(320, 170))
      carImgLabel = customtkinter.CTkLabel(carFrame, image=carImg, text='')
      carImgLabel.place(x=20, y=130)

      carManu = customtkinter.CTkLabel(carFrame, text=car['manufacturer'], font=('Helvetica', 16, 'bold'), text_color='black')
      carManu.place(relx=0.5, rely=0.55, anchor='center')

      carModel = customtkinter.CTkLabel(carFrame, text=car['model'], font=('Helvetica', 24, 'bold'), text_color='black')
      carModel.place(relx=0.5, rely=0.6, anchor='center')


      carBtn = customtkinter.CTkButton(carFrame, command=lambda selectedCar=car: self.rentCarCallBack(selectedCar), text='Rent', font=('Helvetica', 24, 'bold'), fg_color=self.mainClr, text_color='black', corner_radius=16, width=200, height=50)
      carBtn.place(x=75, y=520)