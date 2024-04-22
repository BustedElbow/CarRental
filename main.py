import customtkinter as tk

root = tk.CTk()
root.title("Login Page")
root.geometry('700x500')

tk.set_appearance_mode('light')

btn = tk.CTkButton(master=root, text='Login', corner_radius=8, fg_color='blue', hover_color='red')

btn.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()