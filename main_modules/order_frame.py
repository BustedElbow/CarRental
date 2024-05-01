import customtkinter

class orderFrame(customtkinter.CTkFrame):
  def __init__(self, master, frame_color, main_color, prev_frame):
    super().__init__(master, width = 1450, height = 900, fg_color = frame_color)

    self.previousFrame = prev_frame

    self.main_heading = customtkinter.CTkLabel(self, text = 'Ordering Information', font = ('Helvetica', 36, 'bold'), text_color = main_color)
    self.main_heading.place(x = 130, y = 20)

    self.back_btn = customtkinter.CTkButton(self, text = 'Back', font = ('Helvetica', 16, 'bold'), command = self.show_prev_frame, width = 50, height = 50, corner_radius = 50 // 2, fg_color = main_color)
    self.back_btn.place(x = 20, y = 20)

    self.main_frame = customtkinter.CTkFrame(self, width = 500, height = 500, corner_radius = 16, fg_color = 'white')
    self.main_frame.place(x = 200, y = 200)

    self.car_test = customtkinter.CTkLabel(self.main_frame, text = '', font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.car_test.place(x = 50, y = 50)

  def update_car_model(self, model, manufacturer):
    self.car_test.configure(text = f'Selected Car: {manufacturer} {model}')

  def show_prev_frame(self):
    self.previousFrame.tkraise()