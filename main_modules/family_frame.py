import customtkinter
from tkinter import ttk
from PIL import Image
import os

class familyFrame(customtkinter.CTkFrame):
  def show_prev_frame(self):
    self.previousFrame.tkraise()

  def rent_car_callback(self, selected_car):
    self.orderFrame.update_car_model(selected_car['model'], selected_car['manufacturer'], selected_car['price'])
    self.orderFrame.tkraise()
    
  def __init__(self, master, main_color, frame_color, previousFrame, orderFrame, cars):
    super().__init__(master, width = 1450, height = 900, corner_radius = 0, fg_color = frame_color)

    self.main_color = main_color
    self.orderFrame = orderFrame
    self.previousFrame = previousFrame

    self.main_heading = customtkinter.CTkLabel(self, text = 'Vehicle List', font = ('Helvetica', 36, 'bold'), text_color = main_color)
    self.main_heading.place(x = 130, y = 20)

    self.back_btn = customtkinter.CTkButton(self, text = 'Back', font = ('Helvetica', 16, 'bold'), command = self.show_prev_frame, width = 50, height = 50, corner_radius = 50 // 2, fg_color = main_color)
    self.back_btn.place(x = 20, y = 20)

    self.canvas = customtkinter.CTkCanvas(self, bg = frame_color, width = 1450, height = 815, highlightthickness = 0, scrollregion = (0, 0, 1000, 2780))
    self.canvas.place(x = 1, y = 85)

    self.scrollbar=ttk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
    self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

    self.canvas.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -60), 'units'))
    self.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -60), 'units'))

    self.canvas.config(yscrollcommand = self.scrollbar.set)

    self.cars = cars

    self.main_dir = os.path.dirname(os.path.realpath(__file__))
    self.folder_path = os.path.join(self.main_dir, '../images/family')

    self.createFrames()


  def createFrames(self):
    frame_width = 350
    frame_height = 600
    frame_padding_x = 90
    frame_padding_y = 90
    columns = 3

    for i, car in enumerate(self.cars):
      column_index = i % columns
      row_index = i // columns

      x_position = 130 + column_index * (frame_width + frame_padding_x)
      y_position = -20 + frame_padding_y + row_index * (frame_height + frame_padding_y)

      car_frame = customtkinter.CTkFrame(self.canvas, fg_color = 'white', width = frame_width, height = frame_height, corner_radius = 16)
      self.canvas.create_window((x_position, y_position), window = car_frame, anchor = 'nw')

      car_img_path = os.path.join(self.folder_path, f'{car["manufacturer"].lower()}{car["model"].replace(' ', '_').lower()}.jpg')
      car_img = customtkinter.CTkImage(light_image = Image.open(car_img_path), size = (320, 170))
      car_img_label = customtkinter.CTkLabel(car_frame, image = car_img, text = '')
      car_img_label.place(x = 20, y = 130)

      car_manu = customtkinter.CTkLabel(car_frame, text = car['manufacturer'], font = ('Helvetica', 16, 'bold'), text_color = 'black')
      car_manu.place(relx = 0.5, rely = 0.55, anchor = 'center')

      car_model = customtkinter.CTkLabel(car_frame, text = car['model'], font = ('Helvetica', 24, 'bold'), text_color = 'black')
      car_model.place(relx = 0.5, rely = 0.59, anchor = 'center')

      car_transmission = customtkinter.CTkLabel(car_frame, text=car['transmission'], font=('Helvetica', 16, 'bold'), text_color=self.main_color)
      car_transmission.place(relx=0.5, rely=0.66, anchor='center')

      car_fuel = customtkinter.CTkLabel(car_frame, text=car['fuel'], font=('Helvetica', 16, 'bold'), text_color=self.main_color)
      car_fuel.place(relx=0.5, rely=0.70, anchor='center')

      car_seats = customtkinter.CTkLabel(car_frame, text=f'{car['seats']} seats', font=('Helvetica', 16, 'bold'), text_color=self.main_color)
      car_seats.place(relx=0.5, rely=0.74, anchor='center')

      car_price = customtkinter.CTkLabel(car_frame, text=f'₱ {car['price']} / day', font=('Helvetca', 24, 'bold'), text_color=self.main_color)
      car_price.place(relx=0.5, rely=0.83, anchor='center')

      car_btn = customtkinter.CTkButton(car_frame, command = lambda selected_car = car: self.rent_car_callback(selected_car), text = 'Rent', font = ('Helvetica', 24, 'bold'), fg_color = self.main_color, text_color = 'black', corner_radius = 16, width = 200, height = 50)
      car_btn.place(x = 75, y = 520)





    