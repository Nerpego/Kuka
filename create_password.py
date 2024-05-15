import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import hashlib
import password_scr

# Получение хеша из строки
def get_hash(str):
   hash_object = hashlib.sha256()
   hash_object.update(str.encode())
   hex_digest = hash_object.hexdigest()
   return hex_digest

# Строка содержит только цифры и буквы
def is_num_alpha(str):
   for char in str:
      if not( (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
         print(char)
         return False
         
   return True

# Строка содержит хотя бы одну букву в верхнем регистре
def has_upperAlpha(str):
   for char in str:
      if char.isupper():
         return True
   return False

# Срока содержит хотя бы одну цифру
def has_digit(str):
   for char in str:
      if char.isdigit():
         return True
   return False

def btn_1_click(entry_1, entry_2, cr_pass_root):
   text_1 = entry_1.get()
   text_2 = entry_2.get()

   
   if len(text_1) >= 8 and len(text_2) >= 8:
      if text_1 == text_2:
         if is_num_alpha(text_1):
            if has_digit(text_1):
               if has_upperAlpha(text_1):
                  messagebox.showerror("Успех", "Пароль создан")
                  with open("password.txt", "w") as pass_file:
                     pass_file.writelines(get_hash(text_1))
                  cr_pass_root.destroy()
                  password_scr.run_pass_root()
               else:
                  messagebox.showerror("Ошибка", "Строка должна содержать хотя бы одну заглавную букву")
            else:
               messagebox.showerror("Ошибка", "Пароль должен содержать хотябы одну цифру")
         else:
            messagebox.showerror("Ошибка", "Пароли должны содержать только цифры и буквы латинского алфавита")
      else:
         messagebox.showerror("Ошибка", "Пароли не совпадают")
   else:
      messagebox.showerror("Ошибка", "Длина пароля не менее восьми символов")



def run_cr_pass_root():
   cr_pass_root = tk.Tk()
   cr_pass_root.title("Создание пароля")
   cr_pass_root.geometry("250x300+650+200")
   cr_pass_root.resizable(False, False)
   my_font = Font(size = 14)

   label_1 = tk.Label(cr_pass_root, text="Введите пароль", font=my_font)
   label_1.place(x=50, y=30)

   entry_1 = tk.Entry(cr_pass_root, width=13, font=my_font)
   entry_1.place(x=50, y=70)

   label_2 = tk.Label(cr_pass_root, text="Подтвердите пароль", font=my_font)
   label_2.place(x=28, y=110)

   entry_2 = tk.Entry(cr_pass_root, width=13, font=my_font)
   entry_2.place(x=50, y=140)

   btn_1   = tk.Button(cr_pass_root, text="Подтвердить", command=lambda: btn_1_click(entry_1, entry_2, cr_pass_root), width=13, height=2, font=my_font)
   btn_1.place(x=50, y=200)

   cr_pass_root.mainloop()
