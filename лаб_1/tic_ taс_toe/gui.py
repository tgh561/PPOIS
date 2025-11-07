import tkinter as tk
from tkinter import messagebox
from Field import Field
from Brains import Brains

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")

        self.field = Field()
        self.current_player = "X"

        self.buttons = []
        for i in range(9):
            btn = tk.Button(root, text="", font=("Arial", 32, "bold"),
                            width=3, height=1, command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        self.reset_button = tk.Button(root, text="Сбросить игру", font=("Arial", 14),
                                      command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def make_move(self, index):
        if not self.field.field[index].is_empty():
            messagebox.showinfo("Ошибка", "Ячейка уже занята!")
            return

        self.field.move(index, self.current_player)
        self.buttons[index]["text"] = self.current_player

        winner = Brains.check_winner(self.field)
        if winner:
            if winner == "draw":
                messagebox.showinfo("Итог", "Ничья!")
            else:
                messagebox.showinfo("Итог", f"Победил {winner}!")
            self.disable_buttons()
            return

        self.current_player = "O" if self.current_player == "X" else "X"

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.field.reset_field()
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
