def create_kuka_file(X, Y, Z, A, B, C, S, T):
   kuka_file_text = [
      "&ACCESS RVP",
      "&REL 1",
      "&PARAM EDITMASK = *",
      "&COMENT \" Пример перемещение манипулятора KUKA в указанную позицию \" ",
      "",
      "DEF MoveToPosition()",
      "",
      "  ; Объявление переменной для позиции",
      "  DECL E6POS targetPos",
      f"  targetPos = {{X {X}, Y {Y}, Z {Z}, A {A}, B {B}, C {C}, S {S}, T {T}}}",
      "",
      "END"
   ]
   with open ("kuka_file.txt", 'w') as kuka_file:
      for line in kuka_file_text:
         kuka_file.write(line + '\n')