import customtkinter
import os
from PIL import Image


class checkoutFrame(customtkinter.CTkFrame):
  def __init__(self, master, frame_color, main_color):
    super().__init__(master, width=1450, height=900, corner_radius=0, fg_color=frame_color)

    
    self.class_label = customtkinter.CTkLabel(self, text ='Checkout Successful!', font = ('Helvetica', 48, 'bold'), text_color ='green')
    self.class_label.place(x = 500, y = 280)
    
    self.main_dir = os.path.dirname(os.path.realpath(__file__))
    self.folder_path = os.path.join(self.main_dir, '../images')
    self.image_path = os.path.join(self.folder_path, 'checkout.png')

    self.check_img = customtkinter.CTkImage(light_image = Image.open(self.image_path), size = (150,175))
    self.check_img_label=customtkinter.CTkLabel(self, image = self.check_img, text = '')
    self.check_img_label.place(x = 680, y = 360)