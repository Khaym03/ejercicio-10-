import os
import time


def clear_window():
    os.system("cls")


class Student:
    def __init__(self) -> None:
        self.read_student()

    def read_student(self):
        self.name = input("Ingrese su nombre: ")
        self.ci = input("Ingrese su CI: ")
        clear_window()


class Notes:
    notes = []

    def __init__(self) -> None:
        self.read_notes()

    def read_notes(self):
        while len(self.notes) < 2:
            note = float(input(f"Ingrese la nota {len(self.notes) + 1}: "))

            if note >= 1 or note <= 20:
                self.notes.append(note)
                if len(self.notes) > 1:
                    clear_window()

            else:
                print(f"la nota {note} no esta dentro del rango valido 1-20")
                time.sleep(2)
                clear_window()

    def clear_notes(self):
        self.notes.clear()

    def calc(self, cut: int):
        if cut == 1 or cut == 2:
            return [self.notes[0] * 0.1, self.notes[1] * 0.2]
        if cut == 3:
            return [self.notes[0] * 0.2, self.notes[1] * 0.2]


class Cut:
    def __init__(self):
        self.read_cut()

    def read_cut(self):
        valid_options = [1, 2, 3]
        while True:
            print("Seleccione un corte (1, 2 o 3) -> (Press Enter)")
            print("1 - Primer corte.")
            print("2 - Segundo corte.")
            print("3 - Tercer corte.")

            self.cut = int(input())

            if self.cut not in valid_options:
                print("Opcion no valida intente otra vez.")
            else:
                clear_window()
                break

            time.sleep(2)
            clear_window()


def valid_option() -> bool:
    while True:
        print("Deseas hacer otra consulta?")
        print("1 - Para si.")
        print("0 - Para no.")

        option = input()

        if option == "1":
            return True
        if option == "0":
            return False

        print("Opcion no valida.")
        time.sleep(1.5)


while True:
    student = Student()
    cut = Cut()
    notes = Notes()
    calculated_notes = notes.calc(cut.cut)
    total = sum(calculated_notes)

    print(student.name)
    print(student.ci)
    print(f"Primera evaluacion {notes.notes[0]}pts -> {calculated_notes[0]}pts")
    print(f"Segunda evaluacion {notes.notes[1]}pts -> {calculated_notes[1]}pts")
    print(f"Obteniendo un total de {total}pts")

    notes.clear_notes()

    next = valid_option()
    if next:
        clear_window()
    else:
        break
