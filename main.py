import customtkinter

class mainWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 1600) // 2  
    y = (screen_height - 900) // 2

    self.geometry(f'1600x900+{x}+{y}')
   
    self.title('RMJ Rentals')

    self.frame=customtkinter.CTkFrame(self, width=200, height=200, fg_color='blue', corner_radius=16) 
    self.frame.place(relx=0.5, rely=0.5, anchor='center')

    self._set_appearance_mode('dark')
    self.label=customtkinter.CTkLabel(self.frame, text='FUCK')
    self.label.place(x=10, y=10)

    self.mainloop()


