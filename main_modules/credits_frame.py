import customtkinter
import os
from PIL import Image

class creditsFrame(customtkinter.CTkFrame):
  def __init__(self, master, frame_color, main_color):
    super().__init__(master, width = 1450, height = 900, corner_radius = 0, fg_color = frame_color)
    
    self.class_label = customtkinter.CTkLabel(self, text = 'Credits', font = ('Helvetica', 36, 'bold'), text_color = main_color)
    self.class_label.place(x = 130, y = 20)

    self.main_dir = os.path.dirname(os.path.realpath(__file__))
    self.folder_path = os.path.join(self.main_dir, '../images')
    self.image_path = os.path.join(self.folder_path, 'profile.png')
    
    #First
    self.first_card_frame = customtkinter.CTkFrame(self, width = 350, height = 600, fg_color = 'white', corner_radius = 16)
    self.first_card_frame.place(x = 130, y = 160)

    self.first_img = customtkinter.CTkImage(light_image = Image.open(self.image_path), size = (210,170))
    self.first_img_label=customtkinter.CTkLabel(self.first_card_frame, image = self.first_img, text = '')
    self.first_img_label.place(relx= 0.5, rely = 0.2, anchor='center')
  
    self.first_label = customtkinter.CTkLabel(self.first_card_frame, text = 'Tan, \nMiguel Andrei', font = ('Helvetica', 32, 'bold'), text_color = main_color)
    self.first_label.place(relx=0.5, rely = 0.4, anchor='center')

    self.first_email = customtkinter.CTkLabel(self.first_card_frame, text = 'maevenr81@gmail.com', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.first_email.place(relx = 0.5, rely = 0.5, anchor='center')

    self.first_desc = customtkinter.CTkLabel(self.first_card_frame, text = 'Concept/Idea Specialist', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.first_desc.place(relx = 0.5, rely = 0.6, anchor='center')

    #Second
    self.second_card_frame = customtkinter.CTkFrame(self, width = 350, height = 600, fg_color = 'white', corner_radius = 16)
    self.second_card_frame.place(x = 565, y = 160)

    self.second_img = customtkinter.CTkImage(light_image = Image.open(self.image_path), size = (210,170))
    self.second_img_label=customtkinter.CTkLabel(self.second_card_frame, image = self.second_img, text = '')
    self.second_img_label.place(relx= 0.5, rely = 0.2, anchor='center')
  
    self.second_label = customtkinter.CTkLabel(self.second_card_frame, text = 'Penional, \nRheniel', font = ('Helvetica', 32, 'bold'), text_color = main_color)
    self.second_label.place(relx=0.5, rely = 0.4, anchor='center')

    self.second_email = customtkinter.CTkLabel(self.second_card_frame, text = 'rhenpen@gmail.com', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.second_email.place(relx = 0.5, rely = 0.5, anchor='center')

    self.second_desc = customtkinter.CTkLabel(self.second_card_frame, text = 'Python Programmer', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.second_desc.place(relx = 0.5, rely = 0.6, anchor='center')

    #Third
    self.third_card_frame = customtkinter.CTkFrame(self, width = 350, height = 600, fg_color = 'white', corner_radius = 16)
    self.third_card_frame.place(x = 1000, y = 160)

    self.third_img = customtkinter.CTkImage(light_image = Image.open(self.image_path), size = (210,170))
    self.third_img_label=customtkinter.CTkLabel(self.third_card_frame, image = self.third_img, text = '')
    self.third_img_label.place(relx= 0.5, rely = 0.2, anchor='center')
  
    self.third_label = customtkinter.CTkLabel(self.third_card_frame, text = 'Parantar, \nJohn Kerl', font = ('Helvetica', 32, 'bold'), text_color = main_color)
    self.third_label.place(relx=0.5, rely = 0.4, anchor='center')

    self.third_email = customtkinter.CTkLabel(self.third_card_frame, text = 'j.parantar.535033@gmail.com', wraplength = 230, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.third_email.place(relx = 0.5, rely = 0.5, anchor='center')

    self.third_desc = customtkinter.CTkLabel(self.third_card_frame, text = 'Data Gatherer', wraplength = 220, font = ('Helvetica', 16, 'bold'), text_color = 'black')
    self.third_desc.place(relx = 0.5, rely = 0.6, anchor='center')