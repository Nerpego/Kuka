import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import create_password
import main_menu

def btn_1_click(entry_1, pass_root):
   with open("password.txt", "r") as pass_file:
      pass_hash = pass_file.readline()
   if create_password.get_hash(entry_1.get()) == pass_hash:
      messagebox.showerror("Успех", "Пароль подходит")
      pass_root.destroy()
      main_menu.run_main_menu_scr()
   else:
      messagebox.showerror("Неудача", "Пароль не подходит")
      
def run_pass_root():

   pass_root = tk.Tk()
   pass_root.title("Вход")
   pass_root.geometry("250x300+650+200")
   pass_root.resizable(False, False)
   my_font = Font(size = 14)

   label_1 = tk.Label(pass_root, text="Введите пароль", font=my_font)
   label_1.place(x=50, y=30)

   entry_1 = tk.Entry(pass_root, width=13, font=my_font)
   entry_1.place(x=50, y=70)

   btn_1   = tk.Button(pass_root, text="Вход", command= lambda: btn_1_click(entry_1, pass_root), width=13, height=3, font=my_font)
   btn_1.place(x=50, y=150)

   pass_root.mainloop()
