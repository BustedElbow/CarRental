import customtkinter
from tkinter import ttk
from PIL import Image
import os
from .checkout_frame import rentCar


class familyFrame(customtkinter.CTkFrame):
  def showPreviousFrame(self):
    self.previousFrame.tkraise()

  def rentCarCallBack(self, selectedCar):
    self.checkFrame.updateCarModel(selectedCar['model'], selectedCar['manufacturer'])
    self.checkFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, previousFrame, checkFrame, cars):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.checkFrame=checkFrame
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

    self.famMainDir = os.path.dirname(os.path.realpath(__file__))
    self.famFolderPath = os.path.join(self.famMainDir, '../images/family')

    self.createFrames()

  def createFrames(self):
    frame_width = 350
    frame_height = 600
    frame_padding_x = 90
    frame_padding_y = 90
    columns = 3

    x_main_heading = 130
    x_position_first_column = x_main_heading

    for i, car in enumerate(self.cars):
      column_index = i % columns
      row_index = i // columns

      x_position = x_position_first_column + column_index * (frame_width + frame_padding_x)
      y_position = frame_padding_y + row_index * (frame_height + frame_padding_y)

      carFrame = customtkinter.CTkFrame(self.canvas, fg_color='white', width=frame_width, height=frame_height, corner_radius=16)
      self.canvas.create_window((x_position, y_position), window=carFrame, anchor='nw')

      carImagePath = os.path.join(self.famFolderPath, f'{car["manufacturer"].lower()}{car["model"].lower()}.jpg')
      carImg = customtkinter.CTkImage(light_image=Image.open(carImagePath), size=(320, 170))
      carImgLabel = customtkinter.CTkLabel(carFrame, image=carImg, text='')
      carImgLabel.place(x=20, y=130)

      carManu = customtkinter.CTkLabel(carFrame, text=car['manufacturer'], font=('Helvetica', 16, 'bold'), text_color='black')
      carManu.place(relx=0.5, rely=0.55, anchor='center')

      carModel = customtkinter.CTkLabel(carFrame, text=car['model'], font=('Helvetica', 24, 'bold'), text_color='black')
      carModel.place(relx=0.5, rely=0.6, anchor='center')


      carBtn = customtkinter.CTkButton(carFrame, command=lambda selectedCar=car: self.rentCarCallBack(selectedCar), text='Rent', font=('Helvetica', 24, 'bold'), fg_color=self.mainClr, text_color='black', corner_radius=16, width=200, height=50)
      carBtn.place(x=75, y=520)





    