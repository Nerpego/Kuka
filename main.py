import tkinter as tk
import password_scr
import create_password
import main_menu
import os
from tkinter import messagebox

# Если файл с паролем существует и он не пстой, то перейти в вводу пароля
# Иначе создать пароль
if os.path.isfile("password.txt"):  

   with open("password.txt", "r") as pass_file:
      pass_file_content = pass_file.read()
      if pass_file_content.strip():
         password_scr.run_pass_root()
      else:
         print("Файл пуст")
         create_password.run_cr_pass_root()
         
else:
    print("Файл не существует")
    create_password.run_cr_pass_root()
