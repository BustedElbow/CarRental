import customtkinter
from main_modules.classification_frame import classificationFrame
from main_modules.side_frame import sideFrame
from main_modules.family_frame import familyFrame
from main_modules.vacation_frame import vacationFrame
from main_modules.mover_frame import moverFrame

class mainWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width - 1600) // 2  
    y = (screen_height - 900) // 2
    self._set_appearance_mode('dark')
    self.resizable(False, False)

    mainClr = '#4B9AF6'
    actClr = '#1C3076'
    frameClr = '#242424'

    self.geometry(f'1600x900+{x}+{y}')
   
    self.title('RMJ Car Rentals')


    self.sideFrame=sideFrame(self, fg_color=mainClr)
    self.sideFrame.place(relx=0, rely=0.5, anchor='w')

    self.famFrame=familyFrame(self, frameClr=frameClr, mainClr=mainClr, previousFrame=None)
    self.famFrame.place(relx=1, rely=0.5, anchor='e')

    self.vacFrame=vacationFrame(self, frameClr=frameClr, mainClr=mainClr, previousFrame=None)
    self.vacFrame.place(relx=1, rely=0.5, anchor='e')

    self.movFrame=moverFrame(self, frameClr=frameClr, mainClr=mainClr, previousFrame=None)
    self.movFrame.place(relx=1, rely=0.5, anchor='e')

    self.clsfMainFrame=classificationFrame(self, mainClr=mainClr, frameClr=frameClr, familyFrame=self.famFrame, vacationFrame=self.vacFrame, moverFrame=self.movFrame)
    self.clsfMainFrame.place(relx=1, rely=0.5, anchor='e')

    self.vacFrame.previousFrame=self.clsfMainFrame
    self.famFrame.previousFrame=self.clsfMainFrame
    self.movFrame.previousFrame=self.clsfMainFrame

    self.mainloop()

mainWindow()