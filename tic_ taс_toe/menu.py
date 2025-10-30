from Field import Field
from Brains import Brains

class Menu:
    def __init__(self):
        self.field = Field()
        self.brains = Brains()
        self.current_player = "X"

    def show_main_menu(self):
        print("=== Welcome to Tic-Tac-Toe ===")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            self.start_game()
        elif choice == "2":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Try again.")
            self.show_main_menu()

    def start_game(self):
        self.field.reset_field()
        self.current_player = "X"
        self.game_loop()

    def game_loop(self):
        while True:
            self.display_field()
            print(f"Player {self.current_player}'s turn.")
            index = self.ask_for_move()

            if self.field.move(index, self.current_player):
                result = self.brains.check_winner(self.field)
                if result in ("X", "O"):
                    self.display_field()
                    print(f"Player {result} wins!")
                    break
                elif result == "draw":
                    self.display_field()
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move. Try again.")

        self.ask_restart()

    def ask_for_move(self):
        while True:
            try:
                index = int(input("Enter cell number (0–8): "))
                if 0 <= index <= 8:
                    return index
                else:
                    print("Index must be between 0 and 8.")
            except ValueError:
                print("Please enter a valid number.")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def display_field(self):
        state = self.field.played_moves()
        print("\nCurrent board:")
        for row_start in range(0, 9, 3):
            row_cells = []
            for offset, cell in enumerate(state[row_start:row_start + 3]):
                if cell is None:
                    row_cells.append(str(row_start + offset))
                else:
                    row_cells.append(cell)
            print(" | ".join(row_cells))
        print()

    def ask_restart(self):
        choice = input("Play again? (y/n): ").lower()
        if choice == "y":
            self.start_game()
        else:
            print("Thanks for playing!")
            exit()
