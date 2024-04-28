import customtkinter
from tkinter import ttk

class vacationFrame(customtkinter.CTkFrame):
  def showPreviousFrame(self):
    self.previousFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, previousFrame):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.previousFrame=previousFrame

    self.mainHeading=customtkinter.CTkLabel(self, text='Vehicle List', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.mainHeading.place(x=130, y=20)

    self.backBtn=customtkinter.CTkButton(self, text='Back', font=('Helvetica', 16, 'bold'), command=self.showPreviousFrame, width=50, height=50, corner_radius=50 // 2)
    self.backBtn.place(x=20, y=20)

    self.canvas=customtkinter.CTkCanvas(self, bg=frameClr, width=1450, height=815, highlightthickness=0, scrollregion=(0, 0, 1000, 1420))
    self.canvas.place(x=1, y=85)

    self.scrollbar=ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
    self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    self.canvas.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -60), 'units'))
    self.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -60), 'units'))

    self.canvas.config(yscrollcommand=self.scrollbar.set)

    self.carFrame=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.canvas.create_window((130, 75), window=self.carFrame, anchor='nw')

    self.carFrame2=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.canvas.create_window((565, 75), window=self.carFrame2, anchor='nw')

    self.carFrame3=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.canvas.create_window((1000, 75), window=self.carFrame3, anchor='nw')

    self.carFrame4=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.canvas.create_window((130, 750), window=self.carFrame4, anchor='nw')

    self.carFrame5=customtkinter.CTkFrame(self.canvas, fg_color='white', width=350, height=600, corner_radius=16)
    self.canvas.create_window((565, 750), window=self.carFrame5, anchor='nw')