import customtkinter
import os
from PIL import Image

class classificationFrame(customtkinter.CTkFrame):
  def __init__(self, master, main_color, frame_color, fam_frame, vac_frame, mov_frame):
    super().__init__(master, width = 1450, height = 900, corner_radius = 0, fg_color = frame_color)

    self.class_label = customtkinter.CTkLabel(self, text = 'Vehicle Classification', font = ('Helvetica', 36, 'bold'), text_color = main_color)
    self.class_label.place(x = 130, y = 20)

    self.vacationFrame = vac_frame
    self.familyFrame = fam_frame
    self.moverFrame = mov_frame

    #  Family Frame
    self.fam_card_frame = customtkinter.CTkFrame(self, width = 350, height = 600, fg_color = 'white', corner_radius = 16)
    self.fam_card_frame.place(x = 130, y = 160)

    self.fam_main_dir = os.path.dirname(os.path.realpath(__file__))
    self.fam_folder_path = os.path.join(self.fam_main_dir, '../images/family')
    self.fam_image_path = os.path.join(self.fam_folder_path, 'toyotaInnova.jpg')

    self.fam_img = customtkinter.CTkImage(light_image = Image.open(self.fam_image_path), size = (320,170))
    self.fam_img_label=customtkinter.CTkLabel(self.fam_card_frame, image = self.fam_img, text = '')
    self.fam_img_label.place(x = 20, y = 150)
  
    self.fam_label = customtkinter.CTkLabel(self.fam_card_frame, text = 'Family', font = ('Helvetica', 32, 'bold'), text_color = main_color)
    self.fam_label.place(x = 125, y = 325)

    self.fam_desc = customtkinter.CTkLabel(self.fam_card_frame, text = 'A 4-7 seater vehicle that is realiable and comfortable for family use.', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.fam_desc.place(x = 80, y = 380)

    self.fam_btn = customtkinter.CTkButton(self.fam_card_frame, command = self.show_fam_page, font = ('Helvetica', 24, 'bold'), text = 'View', text_color = 'black', width = 200, height = 50, fg_color = main_color, corner_radius = 16)
    self.fam_btn.place(x = 75, y = 520)

    
    # Vacation Frame
    self.vac_card_frame = customtkinter.CTkFrame(self, width = 350, height = 600, fg_color = 'white', corner_radius = 16)
    self.vac_card_frame.place(x = 565, y = 160)

    ## Vacation Image path
    self.vac_main_dir = os.path.dirname(os.path.realpath(__file__))
    self.vac_folder_path = os.path.join(self.vac_main_dir, '../images/vacation')
    self.vac_image_path = os.path.join(self.vac_folder_path, 'toyotaHiace.jpg')

    self.vac_img = customtkinter.CTkImage(light_image = Image.open(self.vac_image_path), size = (320,220))
    self.vac_img_label = customtkinter.CTkLabel(self.vac_card_frame, image = self.vac_img, text = '')
    self.vac_img_label.place(x = 20, y = 90)

    self.vac_label = customtkinter.CTkLabel(self.vac_card_frame, text = 'Vacation', font = ('Helvetica', 32, 'bold'), text_color = main_color)
    self.vac_label.place(x = 110, y = 325)

    self.vac_desc = customtkinter.CTkLabel(self.vac_card_frame, text = 'A 11-16 seater vehicle good for adventures and vacations.', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.vac_desc.place(x = 75, y = 380)

    self.vac_btn = customtkinter.CTkButton(self.vac_card_frame, command = self.show_vac_page, text = 'View', width = 200, height = 50, fg_color = main_color, font = ('Helvetica', 24, 'bold'), corner_radius = 16, text_color = 'black')
    self.vac_btn.place(x = 75, y = 520)

    # Mover Frame
    self.mov_card_frame = customtkinter.CTkFrame(self, width = 350, height = 600, fg_color = 'white', corner_radius = 16)
    self.mov_card_frame.place(x = 1000, y = 160)

    ## Mover Image Path
    self.mov_main_dir = os.path.dirname(os.path.realpath(__file__))
    self.mov_folder_path = os.path.join(self.mov_main_dir, '../images/mover')
    self.mov_image_path = os.path.join(self.mov_folder_path, 'mazdaBongo.jpg')

    self.mov_img = customtkinter.CTkImage(light_image = Image.open(self.mov_image_path), size = (320,200))
    self.mov_img_label = customtkinter.CTkLabel(self.mov_card_frame, image = self.mov_img, text = '')
    self.mov_img_label.place(x = 20, y = 110)

    self.mov_label = customtkinter.CTkLabel(self.mov_card_frame, text = 'Mover', font = ('Helvetica', 32, 'bold'), text_color = main_color)
    self.mov_label.place(x = 125, y = 325)

    self.mov_desc = customtkinter.CTkLabel(self.mov_card_frame, text = 'A 2 seater vehicle with an opening behind that can carry large objects.', font = ('Helvetica', 16, 'bold'), wraplength = 220, text_color = 'black')
    self.mov_desc.place(x = 80, y = 380)

    self.mov_btn = customtkinter.CTkButton(self.mov_card_frame, command = self.show_mov_page, text = 'View', width = 200, height = 50, fg_color = main_color, font = ('Helvetica', 24, 'bold'), corner_radius = 16, text_color = 'black')
    self.mov_btn.place(x = 75, y = 520)

  def show_vac_page(self):
    self.vacationFrame.tkraise()

  def show_fam_page(self):
    self.familyFrame.tkraise()

  def show_mov_page(self):
    self.moverFrame.tkraise()