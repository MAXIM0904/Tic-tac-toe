class User_game:
    window = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

    def __init__(self, name, simbol):
        self.name = name
        self.simbol = simbol

    def print_window(self):
        print('Игровое поле')
        for i_symbol in self.window:
            print(" ".join(i_symbol))

    def control_coordinates(self, symbol_1):
        if symbol_1 == ".":
            return True
        else:
            print("Место занято!")
            self.game()

    def check_line(self, symbol_1, symbol_2, symbol_3):
        if symbol_1 == self.simbol and symbol_2 == self.simbol and symbol_3 == self.simbol:
            self.print_window()
            print(f"Победа {self.name}")
            return True

    def winner(self):
        for i_srt in range(3):
            if self.check_line(self.window[i_srt][0], self.window[i_srt][1], self.window[i_srt][2]):
                return True
            elif self.check_line(self.window[0][i_srt], self.window[1][i_srt], self.window[2][i_srt]):
                return True
        if self.check_line(self.window[0][0], self.window[1][1], self.window[2][2]):
            return True
        if self.check_line(self.window[2][0], self.window[1][1], self.window[0][2]):
            return True

    def coordinat_control(self):
        try:
            coordinates_x, coordinates_y = input(
                f"{self.name}, введите координаты заполнения через пробел в формате: номер столбца, пробел,"
                f" номер строки: ").split()
        except Exception:
            print("Неверно введены координаты! ")
            while True:
                print("Не будем спешить. Введем координаты поочереди!")
                coordinates_x = int(input(f"Введите номер строки, где хотите поставить знак {self.simbol}: "))
                coordinates_y = int(input(f"Введите номер столбца, где хотите поставить знак {self.simbol}: "))
                print(f"Отлично! В следующий раз вводите просто: {coordinates_x}(пробел){coordinates_y}")
                return coordinates_x, coordinates_y
        else:
            coordinates_x = int(coordinates_x)
            coordinates_y = int(coordinates_y)
            return coordinates_x, coordinates_y

    def game(self):
        self.print_window()
        coordinates_x, coordinates_y = self.coordinat_control()
        if self.control_coordinates(self.window[coordinates_x - 1][coordinates_y - 1]):
            self.window[coordinates_x - 1][coordinates_y - 1] = self.simbol
        return self.winner()


user_1 = User_game("Витя", input("Введите символ,которым будет играть игрок. "))
user_2 = User_game("Саша", input("Введите символ,которым будете играть. "))

while True:
    if user_1.game() is True:
        break
    if user_2.game() is True:
        break

# зачёт! отличная реализация!
