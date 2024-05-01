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

    main_color = '#4B9AF6'
    sec_color = '#1C3076'
    frame_color = '#242424'

    self.geometry(f'1600x900+{x}+{y}')
   
    self.title('RMJ Car Rentals')


    self.sideFrame = sideFrame(self, fg_color = main_color)

    self.famFrame = familyFrame(self, frame_color = frame_color, main_color = main_color, previousFrame = None, orderFrame = None, cars = carsFamily)

    self.vacFrame = vacationFrame(self, frame_color = frame_color, main_color = main_color, previousFrame = None, orderFrame = None, cars = carsVacation)

    self.movFrame = moverFrame(self, frame_color = frame_color, main_color = main_color, previousFrame = None, orderFrame = None, cars = carsMover)

    self.famOrderFrame = orderFrame(self, main_color = main_color, frame_color = frame_color, prev_frame = self.famFrame)

    self.vacOrderFrame = orderFrame(self, main_color = main_color, frame_color = frame_color, prev_frame = self.vacFrame)

    self.movOrderFrame = orderFrame(self, main_color = main_color, frame_color = frame_color, prev_frame = self.movFrame)

    self.clsfMainFrame = classificationFrame(self, main_color = main_color, frame_color = frame_color, fam_frame = self.famFrame, vac_frame = self.vacFrame, mov_frame = self.movFrame)


    self.famFrame.orderFrame = self.famOrderFrame
    self.famFrame.previousFrame = self.clsfMainFrame

    self.vacFrame.orderFrame = self.vacOrderFrame
    self.vacFrame.previousFrame = self.clsfMainFrame
    
    self.movFrame.orderFrame = self.movOrderFrame
    self.movFrame.previousFrame = self.clsfMainFrame

    self.movOrderFrame.place(relx = 1, rely = 0.5, anchor = 'e')
    self.vacOrderFrame.place(relx = 1, rely = 0.5, anchor = 'e')
    self.famOrderFrame.place(relx = 1, rely = 0.5, anchor = 'e')
    self.movFrame.place(relx = 1, rely = 0.5, anchor = 'e')
    self.vacFrame.place(relx = 1, rely = 0.5, anchor = 'e')
    self.famFrame.place(relx = 1, rely = 0.5, anchor = 'e')
    self.sideFrame.place(relx = 0, rely = 0.5, anchor = 'w')
    self.clsfMainFrame.place(relx = 1, rely = 0.5, anchor = 'e')

    self.mainloop()

mainWindow()