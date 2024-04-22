import tkinter as tk

class GUI:

  def __init__(self):

    self.root = tk.Tk()

    self.label = tk.Label(self.root, text='Message my ass')
    self.label.pack()

    self.root.geometry('500x300')

    self.root.mainloop()

GUI()