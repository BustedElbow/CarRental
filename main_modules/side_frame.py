import customtkinter

class sideFrame(customtkinter.CTkFrame):
  def __init__(self, master, fg_color):
    super().__init__(master, width=150, height=900, fg_color=fg_color, corner_radius=0)

    self.about_btn = customtkinter.CTkButton(self, text = 'About', corner_radius = 16, width=110)
    self.about_btn.place(x = 20, y = 850)