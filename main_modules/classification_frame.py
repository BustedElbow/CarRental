import customtkinter
import os
from PIL import Image

class classificationFrame(customtkinter.CTkFrame):
  def showVacPage(self):
    self.vacationFrame.tkraise()

  def showFamPage(self):
    self.familyFrame.tkraise()

  def __init__(self, master, mainClr, frameClr, family_frame, vacation_frame=None):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frameClr)

    self.classlabel=customtkinter.CTkLabel(self, text='Vehicle Classification', font=('Helvetica', 36, 'bold'), text_color=mainClr)
    self.classlabel.place(x=130, y=20)

    self.vacationFrame=vacation_frame
    self.familyFrame=family_frame

    #  Family Frame
    self.famCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.famCardFrame.place(x=130, y=160)

    ## Family Image Path
    self.famMainDir=os.path.dirname(os.path.realpath(__file__))
    self.famFolderPath=os.path.join(self.famMainDir, '../images/family')
    self.famImagePath=os.path.join(self.famFolderPath, 'toyotaInnova.jpg')

    self.famImg=customtkinter.CTkImage(light_image=Image.open(self.famImagePath), size=(320,170))
    self.famImgLabel=customtkinter.CTkLabel(self.famCardFrame, image=self.famImg, text='')
    self.famImgLabel.place(x=20, y=150)
  
    self.famLabel=customtkinter.CTkLabel(self.famCardFrame, text='Family', font=('Helvetica', 32, 'bold'), text_color='black')
    self.famLabel.place(x=125, y=325)

    self.famDesc=customtkinter.CTkLabel(self.famCardFrame, text='A 4-5 seater vehicle that is realiable and comfortable for family use.', wraplength=220, font=('Helvetica', 16, 'bold'), text_color=mainClr)
    self.famDesc.place(x=80, y=380)

    self.famBtn=customtkinter.CTkButton(self.famCardFrame, command=self.showFamPage, font=('Helvetica', 24, 'bold'), text='View', text_color='black', width=200, height=50, fg_color=mainClr, corner_radius=16)
    self.famBtn.place(x=75, y=520)

    
    # Vacation Frame
    self.vacCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.vacCardFrame.place(x=565, y=160)

    ## Vacation Image path
    self.vacMainDir=os.path.dirname(os.path.realpath(__file__))
    self.vacFolderPath=os.path.join(self.vacMainDir, '../images/vacation')
    self.vacImagePath=os.path.join(self.vacFolderPath, 'toyotaHiace.jpg')

    self.vacImg=customtkinter.CTkImage(light_image=Image.open(self.vacImagePath), size=(320,220))
    self.vacImgLabel=customtkinter.CTkLabel(self.vacCardFrame, image=self.vacImg, text='')
    self.vacImgLabel.place(x=20, y=90)

    self.vacLabel=customtkinter.CTkLabel(self.vacCardFrame, text='Vacation', font=('Helvetica', 32, 'bold'), text_color='black')
    self.vacLabel.place(x=110, y=325)

    self.vacDesc=customtkinter.CTkLabel(self.vacCardFrame, text='A 11-16 seater vehicle good for adventures and vacations.', wraplength=220, font=('Helvetica', 16, 'bold'), text_color=mainClr)
    self.vacDesc.place(x=75, y=380)

    self.vacBtn=customtkinter.CTkButton(self.vacCardFrame, command=self.showVacPage, text='View', width=200, height=50, fg_color=mainClr, font=('Helvetica', 24, 'bold'), corner_radius=16, text_color='black')
    self.vacBtn.place(x=75, y=520)

    # Mover Frame
    self.movCardFrame=customtkinter.CTkFrame(self, width=350, height=600, fg_color='white', corner_radius=16)
    self.movCardFrame.place(x=1000, y=160)

    ## Mover Image Path
    self.movMainDir=os.path.dirname(os.path.realpath(__file__))
    self.movFolderPath=os.path.join(self.movMainDir, '../images/mover')
    self.movImagePath=os.path.join(self.movFolderPath, 'mazdaBongo.jpg')

    self.movImg=customtkinter.CTkImage(light_image=Image.open(self.movImagePath), size=(320,200))
    self.movImgLabel=customtkinter.CTkLabel(self.movCardFrame, image=self.movImg, text='')
    self.movImgLabel.place(x=20, y=110)

    self.movLabel=customtkinter.CTkLabel(self.movCardFrame, text='Mover', font=('Helvetica', 32, 'bold'), text_color='black')
    self.movLabel.place(x=125, y=325)

    self.movDesc=customtkinter.CTkLabel(self.movCardFrame, text='A 2 seater vehicle with an opening behind that can carry large objects.', font=('Helvetica', 16, 'bold'), wraplength=220, text_color=mainClr)
    self.movDesc.place(x=80, y=380)

    self.movBtn=customtkinter.CTkButton(self.movCardFrame, text='View', width=200, height=50, fg_color=mainClr, font=('Helvetica', 24, 'bold'), corner_radius=16, text_color='black')
    self.movBtn.place(x=75, y=520)
