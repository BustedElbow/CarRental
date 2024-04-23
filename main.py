import customtkinter

class mainWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 800) // 2  
    y = (screen_height - 450) // 2

    self.geometry(f'600x600+{x}+{y}')
   
    self.title('RMJ Rentals')

    self.frame=customtkinter.CTkFrame(self, width=200, height=200, fg_color='blue', corner_radius=16) 
    self.frame.place(relx=0.5, rely=0.5, anchor='center')

    self._set_appearance_mode('dark')
    self.label=customtkinter.CTkLabel(self.frame, text='FUCK')
    self.label.place(x=10, y=10)

    self.mainloop()


