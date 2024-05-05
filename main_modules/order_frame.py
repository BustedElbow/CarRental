import customtkinter
import datetime

class orderFrame(customtkinter.CTkFrame):
  def __init__(self, master, frame_color, main_color, prev_frame):
    super().__init__(master, width = 1450, height = 900, fg_color = frame_color)

    self.previousFrame = prev_frame

    self.main_heading = customtkinter.CTkLabel(self, text = 'Ordering Information', font = ('Helvetica', 36, 'bold'), text_color = main_color)
    self.main_heading.place(x = 130, y = 20)

    self.back_btn = customtkinter.CTkButton(self, text = 'Back', font = ('Helvetica', 16, 'bold'), command = self.show_prev_frame, width = 50, height = 50, corner_radius = 50 // 2, fg_color = main_color)
    self.back_btn.place(x = 20, y = 20)
    
    self.car_price = 0

    # Options Frame Components
    self.options_frame = customtkinter.CTkFrame(self, width = 850, height = 500, corner_radius = 16, fg_color = 'white')
    self.options_frame.place(x = 130, y = 200)

    self.pickup_label = customtkinter.CTkLabel(self.options_frame, text='Pickup Date', font=('Helvetica', 16, 'bold'), text_color='black')
    self.pickup_label.place(x=50, y=20)

    self.pickup_date_entry = customtkinter.CTkEntry(self.options_frame, width=200, placeholder_text="MM-DD-YYYY")
    self.pickup_date_entry.place(x=50, y=50)
    self.pickup_date_entry.bind("<KeyRelease>", self.on_date_change)  

    self.return_label = customtkinter.CTkLabel(self.options_frame, text='Return Date', font=('Helvetica', 16, 'bold'), text_color='black')
    self.return_label.place(x=300, y=20)

    self.return_date_entry = customtkinter.CTkEntry(self.options_frame, width=200, placeholder_text="MM-DD-YYYY")
    self.return_date_entry.place(x=300, y=50)
    self.return_date_entry.bind("<KeyRelease>", self.on_date_change)  

    # Summary Frame Components
    self.summary_frame = customtkinter.CTkFrame(self, width = 350, height = 600, corner_radius = 16, fg_color = 'white')
    self.summary_frame.place(x = 1010, y = 200)

    self.summary_label = customtkinter.CTkLabel(self.summary_frame, text='Summary', font=('Helvetica', 16, 'bold'), text_color='black')
    self.summary_label.place(x=30, y=20)

    self.summary_btn = customtkinter.CTkButton(self.summary_frame, text='Confirm', font=('Helvetica', 16, 'bold'), fg_color=main_color, text_color='black', corner_radius=16, width=200, height=50)
    self.summary_btn.place(x=75, y=520)

    self.total_price_label = customtkinter.CTkLabel(self.summary_frame, text='Total:', font=('Helvetica', 16, 'bold'), text_color='black')
    self.total_price_label.place(x=30, y=150)
  
    self.total_price = customtkinter.CTkLabel(self.summary_frame, text="₱ 0", font=('Helvetica', 16, 'bold'), text_color=main_color)
    self.total_price.place(x=30, y=170)

    self.get_selected_car = customtkinter.CTkLabel(self.summary_frame, text = '', font = ('Helvetica', 16, 'bold'), text_color = main_color)
    self.get_selected_car.place(x = 30, y = 50)

    self.get_car_price = customtkinter.CTkLabel(self.summary_frame, text='', font = ('Helvetica', 16, 'bold'), text_color = main_color)
    self.get_car_price.place(x = 30, y = 80)


  def update_car_model(self, model, manufacturer, price):
    self.get_selected_car.configure(text = f'{manufacturer} {model}')
    self.get_car_price.configure(text = f'₱ {price} / day')
    self.car_price = price

  def show_prev_frame(self):
    if self.return_date_entry.get() != '':
      self.return_date_entry.delete(0, 10)
        
    if self.pickup_date_entry.get() != '':
      self.pickup_date_entry.delete(0, 10)
      
    self.total_price.configure(text="₱ 0")
    self.previousFrame.tkraise()
  
  def on_date_change(self, event):
    self.calculate_total_price()

  def calculate_total_price(self):
    try:
      pickup_date_str = self.pickup_date_entry.get()
      return_date_str = self.return_date_entry.get()

      pickup_date = datetime.datetime.strptime(pickup_date_str, "%m-%d-%Y")
      return_date = datetime.datetime.strptime(return_date_str, "%m-%d-%Y")

      rental_duration = (return_date - pickup_date).days

      if rental_duration > 7:
        self.total_price.configure(text="Invalid Date: Duration is capped at 7 days")
        return 
      
      if rental_duration <= 0:
        self.total_price.configure(text="Invalid Dates: Duration must be positive")
        return



      total_price = rental_duration * self.car_price

      self.total_price.configure(text=f"₱ {total_price}")

    except ValueError:  
      self.total_price.configure(text="Calculating...")
