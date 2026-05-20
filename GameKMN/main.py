# ЮНУСОВ ПАВЕЛ ИИАД 1

import time
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def make_choice(self):
        while True:
            choice = input(f"{self.name}, твой выбор (камень, ножницы, бумага): ").lower()
            if choice in ["камень", "ножницы", "бумага"]:
                return choice
            print("Неверно! Попробуй ещё раз.")

class Game:

    def __init__(self):
        self.player1 = Player("Игрок 1")
        self.player2 = Player("Игрок 2")

    def hide_previous_choice(self):
        print("\n" * 200)
        print("СЛЕДУЮЩИЙ ИГРОК")
        print("\n" * 5)

    def get_winner(self, choice1, choice2):
        if choice1 == choice2:
            return None

        if (choice1 == "камень" and choice2 == "ножницы") or \
                (choice1 == "ножницы" and choice2 == "бумага") or \
                (choice1 == "бумага" and choice2 == "камень"):
            return self.player1
        else:
            return self.player2

    def play_round(self):
        print(f"Счёт: {self.player1.score} : {self.player2.score} ")

        print("ХОД ИГРОКА 1")
        choice1 = self.player1.make_choice()
        self.hide_previous_choice()

        print(f"Счёт: {self.player1.score} : {self.player2.score}")
        print("ХОД ИГРОКА 2")
        choice2 = self.player2.make_choice()

        print("\nРЕЗУЛЬТАТ")
        print(f"\n{self.player1.name} выбрал: {choice1}")
        print(f"{self.player2.name} выбрал: {choice2}")

        winner = self.get_winner(choice1, choice2)

        if winner is None:
            print("\nНИЧЬЯ!")
        else:
            winner.score += 1
            print(f"\n{winner.name} ВЫИГРЫВАЕТ РАУНД! ")

        print(f"Счёт: {self.player1.score} : {self.player2.score}")

    def play(self):
        print("КАМЕНЬ, НОЖНИЦЫ, БУМАГА")

        input("\nНажми Enter, чтобы начать...\n")

        while True:
            self.play_round()

            if self.player1.score >= 3:
                print(f"ПОБЕДИТЕЛЬ: {self.player1.name}!")
                break
            elif self.player2.score >= 3:
                print(f"ПОБЕДИТЕЛЬ: {self.player2.name}!")
                break

            input("\nНажми Enter для следующего раунда...")

if __name__ == "__main__":
    game = Game()
    game.play()
