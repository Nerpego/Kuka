import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import kuka_file_form

def menu_About():
   messagebox.showinfo("О программе", "Безопасное программное обествечение для удаленного управления промышленным манипулятором. Павлов Григорий Эдуардович БСБО-03-20.")

def menu_Params_X_Y_Z():
   messagebox.showinfo("Переменные X Y Z", f"Пример: \n pos = X, Y, Z, A, B, C, S, T \n X = 500.0: Робот будет перемещён на 500 мм вправо от базовой точки. \n Y = 200.0: Робот будет перемещён на 200 мм вперёд от базовой точки. \n Z = 300.0: Робот будет перемещён на 300 мм вверх от базовой точки.")

def menu_Params_S():
   messagebox.showinfo("Переменная S", f"Пример: \n pos = X, Y, Z, A, B, C, S, T \n Значение S представляется в виде трехбитного двоичного числа, где: \n 0 это локоть высоко|кисть вверх|ориентация TCP \n 1 это локоть низко|кисть вниз|другая ориентация TCP \n Пример: S = 2 => (010) \n локоть высоко|кисть вниз|ориентация TCP" )

def menu_Params_T():
   messagebox.showinfo("Переменная T", f"Пример: \n pos = X, Y, Z, A, B, C, S, T \n Значение T представляется в виде шестибитного двоичного числа, где: \n Биты 0-1 отвечают за ось 6 \n Биты 2-3 отвечают за ось 5 \n Биты 4-5 отвечают за ось 4 \n Пример: T = 35 => 100011 \n Биты 0-1 (11): Означают 3 оборота оси 6 \n Биты 2-3 (00): Означают 0 оборотов оси 5 \n Биты 4-5 (10): Означают 2 оборота оси 4")

def menu_Params_A_B_C():
   messagebox.showinfo("Переменные A B C", f"Пример: \n pos = X, Y, Z, A, B, C, S, T \n Углы A B C измеряюся в градусах и могут принимать значения от -180 до +180 \n A обозначает поворот вокруг оси X \n B обозначает поворот вокруг оси Y \n С обозначает поворот вокруг оси Z")

def check_entry(entry_X,entry_Y,entry_Z,entry_A,entry_B,entry_C,entry_S,entry_T):
   str = entry_X.get()
   if str.isdigit():
      if int(str) >= -1100 and int(str) <= 1100:
         print("X введено верно")
      else:
         messagebox.showerror("Ошибка", "X не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "X должно быть числом")
      return False
   str = entry_Y.get()
   if str.isdigit():
      if int(str) >= -1100 and int(str) <= 1100:
         print("Y введено верно")
      else:
         messagebox.showerror("Ошибка", "Y не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "Y должно быть числом")
      return False
   str = entry_Z.get()
   if str.isdigit():
      if int(str) >= -500 and int(str) <= 2000:
         print("Z введено верно")
      else:
         messagebox.showerror("Ошибка", "Z не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "Z должно быть числом")
      return False
   str = entry_A.get()
   if str.isdigit():
      if int(str) >= -180 and int(str) <= 180:
         print("A введено верно")
      else:
         messagebox.showerror("Ошибка", "A не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "A должно быть числом")
      return False
   str = entry_B.get()
   if str.isdigit():
      if int(str) >= -180 and int(str) <= 180:
         print("B введено верно")
      else:
         messagebox.showerror("Ошибка", "B не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "B должно быть числом")
      return False
   str = entry_C.get()
   if str.isdigit():
      if int(str) >= -180 and int(str) <= 180:
         print("C введено верно")
      else:
         messagebox.showerror("Ошибка", "C не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "C должно быть числом")
      return False
   str = entry_S.get()
   if str.isdigit():
      if int(str) >= 0 and int(str) <= 7:
         print("S введено верно")
      else:
         messagebox.showerror("Ошибка", "S не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "S должно быть числом")
      return False
   str = entry_T.get()
   if str.isdigit():
      if int(str) >= 0 and int(str) <= 63:
         print("T введено верно")
      else:
         messagebox.showerror("Ошибка", "T не попадает в диапазон")
         return False
   else:
      messagebox.showerror("Ошибка", "T должно быть числом")
      return False
   
   return True

def btn_send_click(entry_X,entry_Y,entry_Z,entry_A,entry_B,entry_C,entry_S,entry_T):
   if check_entry(entry_X,entry_Y,entry_Z,entry_A,entry_B,entry_C,entry_S,entry_T):
      kuka_file_form.create_kuka_file(entry_X.get(),entry_Y.get(),entry_Z.get(),entry_A.get(),entry_B.get(),entry_C.get(),entry_S.get(),entry_T.get())

def set_def(entry_X,entry_Y,entry_Z,entry_A,entry_B,entry_C,entry_S,entry_T):
   entry_X.delete(0, tk.END)
   entry_X.insert(0, "0")
   entry_Y.delete(0, tk.END)
   entry_Y.insert(0, "0")
   entry_Z.delete(0, tk.END)
   entry_Z.insert(0, "0")
   entry_A.delete(0, tk.END)
   entry_A.insert(0, "0")
   entry_B.delete(0, tk.END)
   entry_B.insert(0, "0")
   entry_C.delete(0, tk.END)
   entry_C.insert(0, "0")
   entry_S.delete(0, tk.END)
   entry_S.insert(0, "6")
   entry_T.delete(0, tk.END)
   entry_T.insert(0, "35")

def run_main_menu_scr():
   menu_root = tk.Tk()
   menu_root.title("Главное меню")
   menu_root.geometry("800x500+350+200")
   menu_root.resizable(False, False)

   my_font = Font(size = 10)

   menu_bar = tk.Menu(menu_root)
   
   menu_help_part = tk.Menu(menu_bar, tearoff=0)
   menu_help_part.add_command(label="Переменные X Y Z", command=menu_Params_X_Y_Z, font=my_font)
   menu_help_part.add_command(label="Переменные A B C", command=menu_Params_A_B_C, font=my_font)
   menu_help_part.add_command(label="Переменная S", command=menu_Params_S,font=my_font)
   menu_help_part.add_command(label="Переменная T", command=menu_Params_T,font=my_font)

   menu_bar.add_command(label="О программе", command=menu_About, font=my_font)

   menu_bar.add_cascade(label="Помощь", menu=menu_help_part)

   btn_send = tk.Button(menu_root, font=my_font, text="Отправить", width=13, height=3, command=lambda: btn_send_click(entry_X,entry_Y,entry_Z,entry_A,entry_B,entry_C,entry_S,entry_T))
   btn_send.place(x=350, y=400)

   btn_set_def = tk.Button(menu_root, font=my_font, text="HOME", width=13, command=lambda: set_def(entry_X,entry_Y,entry_Z,entry_A,entry_B,entry_C,entry_S,entry_T))
   btn_set_def.place(x=400, y=30)

   label_X = tk.Label(menu_root, text="X = ", font=my_font)
   label_X.place(x=20, y=25)
   label_X_diap = tk.Label(menu_root, text="от -1100 мм до +1100 мм", font=my_font)
   label_X_diap.place(x=175, y=25)

   label_Y = tk.Label(menu_root, text="Y = ", font=my_font)
   label_Y.place(x=20, y=45)
   label_Y_diap = tk.Label(menu_root, text="от -1100 мм до +1100 мм", font=my_font)
   label_Y_diap.place(x=175, y=45)

   label_Z = tk.Label(menu_root, text="Z = ", font=my_font)
   label_Z.place(x=20, y=65)
   label_Z_diap = tk.Label(menu_root, text="от -500 мм до +2000 мм", font=my_font)
   label_Z_diap.place(x=175, y=65)

   label_A = tk.Label(menu_root, text="A = ", font=my_font)
   label_A.place(x=20, y=85)
   label_A_diap = tk.Label(menu_root, text="от -180 до 180", font=my_font)
   label_A_diap.place(x=175, y=85)

   label_B = tk.Label(menu_root, text="B = ", font=my_font)
   label_B.place(x=20, y=105)
   label_B_diap = tk.Label(menu_root, text="от -180 до 180", font=my_font)
   label_B_diap.place(x=175, y=105)

   label_C = tk.Label(menu_root, text="C = ", font=my_font)
   label_C.place(x=20, y=125)
   label_C_diap = tk.Label(menu_root, text="от -180 до 180", font=my_font)
   label_C_diap.place(x=175, y=125)

   label_S = tk.Label(menu_root, text="S = ", font=my_font)
   label_S.place(x=20, y=145)
   label_S_diap = tk.Label(menu_root, text="от 0 до 7", font=my_font)
   label_S_diap.place(x=175, y=145)

   label_T = tk.Label(menu_root, text="T = ", font=my_font)
   label_T.place(x=20, y=165)
   label_T_diap = tk.Label(menu_root, text="от 0 до 63", font=my_font)
   label_T_diap.place(x=175, y=165)

   
   entry_X = tk.Entry(menu_root, width=15, font=my_font)
   entry_X.place(x=60, y=25)

   entry_Y = tk.Entry(menu_root, width=15, font=my_font)
   entry_Y.place(x=60, y=45)

   entry_Z = tk.Entry(menu_root, width=15, font=my_font, )
   entry_Z.place(x=60, y=65)

   entry_A = tk.Entry(menu_root, width=15, font=my_font, )
   entry_A.place(x=60, y=85)

   entry_B = tk.Entry(menu_root, width=15, font=my_font, )
   entry_B.place(x=60, y=105)

   entry_C = tk.Entry(menu_root, width=15, font=my_font, )
   entry_C.place(x=60, y=125)

   entry_S = tk.Entry(menu_root, width=15, font=my_font, )
   entry_S.place(x=60, y=145)

   entry_T = tk.Entry(menu_root, width=15, font=my_font, )
   entry_T.place(x=60, y=165)

   menu_root.config(menu=menu_bar)
   menu_root.mainloop()
