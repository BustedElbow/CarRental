import customtkinter
import datetime
import tkinter.ttk as ttk

class orderFrame(customtkinter.CTkFrame):
  def __init__(self, master, frame_color, main_color, prev_frame):
    super().__init__(master, width = 1450, height = 900, fg_color = frame_color)

    self.previousFrame = prev_frame

    self.pickup_date = 'MMM-DD-YYYY'
    self.return_date = 'MMM-DD-YYYY'

    self.time = ['08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM', '06:00 PM']

    self.main_heading = customtkinter.CTkLabel(self, text = 'Ordering Information', font = ('Helvetica', 36, 'bold'), text_color = main_color)
    self.main_heading.place(x = 130, y = 20)

    self.back_btn = customtkinter.CTkButton(self, text = 'Back', font = ('Helvetica', 16, 'bold'), command = self.show_prev_frame, width = 50, height = 50, corner_radius = 50 // 2, fg_color = main_color)
    self.back_btn.place(x = 20, y = 20)
    
    self.car_price = 0

    # Options Frame Components - Date and Time
    self.options_frame = customtkinter.CTkFrame(self, width = 850, height = 500, corner_radius = 16, fg_color = 'white')
    self.options_frame.place(x = 130, y = 200)

    self.pickup_label = customtkinter.CTkLabel(self.options_frame, text='Pickup Date', font=('Helvetica', 16, 'bold'), text_color='black')
    self.pickup_label.place(x=50, y=20)

    self.pickup_date_entry = customtkinter.CTkEntry(self.options_frame, width=120, placeholder_text="MMM-DD-YYYY")
    self.pickup_date_entry.place(x=50, y=50)
    self.pickup_date_entry.bind("<KeyRelease>", self.on_date_change)  

    self.pickup_time_label = customtkinter.CTkLabel(self.options_frame, text='Pickup Time', font=('Helvetica', 16, 'bold'), text_color='black')
    self.pickup_time_label.place(x=190, y=20)

    self.pickup_time_entry = customtkinter.CTkComboBox(self.options_frame, width=100, values=self.time)
    self.pickup_time_entry.place(x=190, y=50)
   
    self.return_label = customtkinter.CTkLabel(self.options_frame, text='Return Date', font=('Helvetica', 16, 'bold'), text_color='black')
    self.return_label.place(x=350, y=20)

    self.return_date_entry = customtkinter.CTkEntry(self.options_frame, width=120, placeholder_text="MMM-DD-YYYY")
    self.return_date_entry.place(x=350, y=50)
    self.return_date_entry.bind("<KeyRelease>", self.on_date_change)

    self.return_time_label = customtkinter.CTkLabel(self.options_frame, text='Return Time', font=('Helvetica', 16, 'bold'), text_color='black')
    self.return_time_label.place(x=490, y=20) 

    self.return_time_entry = customtkinter.CTkComboBox(self.options_frame, width=100, values=self.time)
    self.return_time_entry.place(x=490, y=50)

    # Options Frame Components - Customer
    self.customer_info_label = customtkinter.CTkLabel(self.options_frame, text='Customer Information', font=('Helvetica', 24, 'bold'), text_color=main_color)
    self.customer_info_label.place(x=50, y=100) 

    self.driver_license = customtkinter.CTkLabel(self.options_frame, text="Driver's License Number", font=('Helvetica', 16, 'bold'), text_color='black')
    self.driver_license.place(x=50, y=130)

    self.driver_license_entry = customtkinter.CTkEntry(self.options_frame, width=200)
    self.driver_license_entry.place(x=50, y=160)

    self.first_name = customtkinter.CTkLabel(self.options_frame, text='First Name', font=('Helvetica', 16, 'bold'), text_color='black')
    self.first_name.place(x=310, y=130)

    self.first_name_entry = customtkinter.CTkEntry(self.options_frame, width=150)
    self.first_name_entry.place(x=310, y=160)

    self.last_name = customtkinter.CTkLabel(self.options_frame, text='Last Name', font=('Helvetica', 16, 'bold'), text_color='black')
    self.last_name.place(x=480, y=130)

    self.last_name_entry = customtkinter.CTkEntry(self.options_frame, width=150)
    self.last_name_entry.place(x=480, y=160)

    self.addon_label = customtkinter.CTkLabel(self.options_frame, text='Add-on', font=('Helvetica', 24, 'bold'), text_color=main_color)
    self.addon_label.place(x=50, y=210)

    self.with_driver_check = customtkinter.CTkCheckBox(self.options_frame, text='With Driver (12 Hours) - ₱ 1000 / day ', font=('Helvetica', 16, 'bold'), text_color='black')
    self.with_driver_check.place(x=50, y=245)

    self.terms_label = customtkinter.CTkLabel(self.options_frame, text='Terms & Condition', font=('Helvetica', 24, 'bold'), text_color=main_color)
    self.terms_label.place(x=50, y=290)

    self.insurance_check = customtkinter.CTkCheckBox(self.options_frame, text='Kamo na isip unsa na sentences ang ibutang diri na about atong insurance/terms \nbullshit blah blah blah', font=('Helvetica', 16, 'bold'), text_color='black')
    self.insurance_check.place(x=50, y=325)



    # Summary Frame Components
    self.summary_frame = customtkinter.CTkFrame(self, width = 350, height = 600, corner_radius = 16, fg_color = 'white')
    self.summary_frame.place(x = 1010, y = 200)

    self.summary_label = customtkinter.CTkLabel(self.summary_frame, text='Summary', font=('Helvetica', 24, 'bold'), text_color=main_color)
    self.summary_label.place(x=30, y=20)

    self.rental_duration_label = customtkinter.CTkLabel(self.summary_frame, text='Rental Duration:', font=('Helvetica', 16, 'bold'), text_color='black')
    self.rental_duration_label.place(x=30, y=50)

    self.rental_duration = customtkinter.CTkLabel(self.summary_frame, text=f'{self.pickup_date} to {self.return_date}', font=('Helvetica', 16, 'bold'), text_color='black')
    self.rental_duration.place(x=30, y=80)

    self.get_selected_car = customtkinter.CTkLabel(self.summary_frame, text = '', font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.get_selected_car.place(x = 30, y = 120)

    self.get_car_price = customtkinter.CTkLabel(self.summary_frame, text='', font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.get_car_price.place(x = 30, y = 140)

    self.total_price_label = customtkinter.CTkLabel(self.summary_frame, text='Total:', font=('Helvetica', 16, 'bold'), text_color='black')
    self.total_price_label.place(x=30, y=180)
  
    self.total_price = customtkinter.CTkLabel(self.summary_frame, text="₱ 0", font=('Helvetica', 16, 'bold'), text_color='black')
    self.total_price.place(x=30, y=200)


    self.checkout_btn = customtkinter.CTkButton(self.summary_frame, text='Checkout', font=('Helvetica', 16, 'bold'), fg_color=main_color, text_color='black', corner_radius=16, width=200, height=50, state=customtkinter.DISABLED)
    self.checkout_btn.place(x=75, y=520)


  def update_car_model(self, model, manufacturer, price):
    self.get_selected_car.configure(text = f'{manufacturer} {model}')
    self.get_car_price.configure(text = f'₱ {price} / day')
    self.car_price = price

  def show_prev_frame(self):
    if self.return_date_entry.get() != '':
      self.return_date_entry.delete(0, 10)
        
    if self.pickup_date_entry.get() != '':
      self.pickup_date_entry.delete(0, 10)
      
    self.total_price.configure(text="₱ 0", text_color='black')
    self.previousFrame.tkraise()
  
  def on_date_change(self, event):
    self.calculate_total_price()

  def calculate_total_price(self):
    try:
      pickup_date_str = self.pickup_date_entry.get()
      return_date_str = self.return_date_entry.get()

      self.pickup_date = self.pickup_date_entry.get()
      self.return_date = self.return_date_entry.get()

      pickup_time_str = self.pickup_time_entry.get()
      return_time_str = self.return_time_entry.get()

      pickup_date = datetime.datetime.strptime(pickup_date_str, "%b-%d-%Y")
      return_date = datetime.datetime.strptime(return_date_str, "%b-%d-%Y")

      pickup_time = datetime.datetime.strptime(pickup_time_str, "%I:%M %p").time()
      return_time = datetime.datetime.strptime(return_time_str, "%I:%M %p").time()

      current_date = datetime.datetime.now()
   
      
      pickup_difference = pickup_date - current_date
      return_difference = return_date - current_date
      
      rental_duration = (return_date - pickup_date).days

      if pickup_date < current_date or return_date < current_date:
        self.total_price.configure(text="Invalid Date", text_color='red')
        return
      else:
        self.total_price.configure(text_color='black')

      if pickup_date == return_date and pickup_time >= return_time:
        self.total_price.configure(text="Return time must be after pickup time", text_color='red')
        return
      else:
        self.total_price.configure(text_color='black')

      if pickup_difference.days > 30 or return_difference.days > 30:
        self.total_price.configure(text="Exceeds Early Booking - Max: 1 month", text_color='red')
        return
      else:
        self.total_price.configure(text_color='black')

      if rental_duration > 7:
        self.total_price.configure(text="Exceeds Duration - Max: 7 days", text_color='red')
        return
      else:
        self.total_price.configure(text_color='black') 
      
      if rental_duration <= 0:
        self.total_price.configure(text="Invalid Duration", text_color='red')
        return
      else:
        self.total_price.configure(text_color='black')


      total_price = rental_duration * self.car_price
      self.rental_duration.configure(text=f'{self.pickup_date} to {self.return_date}')
      self.total_price.configure(text=f"₱ {total_price}")

    except ValueError:  
      self.total_price.configure(text="Calculating...", text_color='black')

  
