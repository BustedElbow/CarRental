import customtkinter
from main_modules.classification_frame import classificationFrame
from main_modules.side_frame import sideFrame
from main_modules.family_frame import familyFrame
from main_modules.vacation_frame import vacationFrame
from main_modules.mover_frame import moverFrame
from main_modules.order_frame import orderFrame
from main_modules.car_profiles import carsFamily, carsVacation, carsMover

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

    self.famFrame=familyFrame(self, frameClr=frameClr, mainClr=mainClr, previousFrame=None, orderFrame=None, cars=carsFamily)
    self.famFrame.place(relx=1, rely=0.5, anchor='e')

    self.vacFrame=vacationFrame(self, frameClr=frameClr, mainClr=mainClr, previousFrame=None, orderFrame=None, cars=carsVacation)
    self.vacFrame.place(relx=1, rely=0.5, anchor='e')

    self.movFrame=moverFrame(self, frameClr=frameClr, mainClr=mainClr, previousFrame=None, orderFrame=None, cars=carsMover)
    self.movFrame.place(relx=1, rely=0.5, anchor='e')

    self.famOrderFrame=orderFrame(self, mainClr=mainClr, frameClr=frameClr, previousFrame=self.famFrame)
    self.famOrderFrame.place(relx=1, rely=0.5, anchor='e')

    self.vacOrderFrame=orderFrame(self, mainClr=mainClr, frameClr=frameClr, previousFrame=self.vacFrame)
    self.vacOrderFrame.place(relx=1, rely=0.5, anchor='e')

    self.movOrderFrame=orderFrame(self, mainClr=mainClr, frameClr=frameClr, previousFrame=self.movFrame)
    self.movOrderFrame.place(relx=1, rely=0.5, anchor='e')

    self.clsfMainFrame=classificationFrame(self, mainClr=mainClr, frameClr=frameClr, familyFrame=self.famFrame, vacationFrame=self.vacFrame, moverFrame=self.movFrame)
    self.clsfMainFrame.place(relx=1, rely=0.5, anchor='e')

    self.vacFrame.previousFrame=self.clsfMainFrame
    self.famFrame.previousFrame=self.clsfMainFrame
    self.movFrame.previousFrame=self.clsfMainFrame
    self.famFrame.orderFrame=self.famOrderFrame
    self.vacFrame.orderFrame=self.vacOrderFrame
    self.movFrame.orderFrame=self.movOrderFrame


    self.mainloop()

mainWindow()