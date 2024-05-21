import customtkinter

class sideFrame(customtkinter.CTkFrame):
  def __init__(self, master, fg_color, home_page, credits_page):
    super().__init__(master, width=150, height=900, fg_color=fg_color, corner_radius=0)

    self.home_page = home_page
    self.credits_page = credits_page

    self.home_btn = customtkinter.CTkButton(self, text='Home', font=('Helvetica', 24, 'bold'), text_color='black', command=self.show_home_page)
    self.home_btn.place(x=6, y= 100)

    self.credits_btn = customtkinter.CTkButton(self, text = 'Credits', corner_radius = 16, width=110, command=self.show_credits_page)
    self.credits_btn.place(x = 20, y = 850)

  def show_home_page(self):
    self.home_page.tkraise()

  def show_credits_page(self):
    self.credits_page.tkraise()
