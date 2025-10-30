import tkinter as tk
from tkinter import messagebox
from Field import Field
from Brains import Brains

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.field = Field()
        self.brains = Brains()
        self.current_player = "X"
        self.buttons = []
        self.status_var = tk.StringVar()
        self._build_ui()
        self._update_status()

    def _build_ui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(padx=10, pady=10)
        board_frame = tk.Frame(top_frame)
        board_frame.grid(row=0, column=0)
        for i in range(9):
            btn = tk.Button(board_frame, text="", width=6, height=3, font=("Helvetica", 20), command=lambda idx=i: self.on_cell_click(idx))
            btn.grid(row=i//3, column=i%3, padx=4, pady=4)
            self.buttons.append(btn)
        right_frame = tk.Frame(top_frame)
        right_frame.grid(row=0, column=1, padx=10, sticky="n")
        status_label = tk.Label(right_frame, textvariable=self.status_var, font=("Helvetica", 12), width=20, anchor="w")
        status_label.pack(pady=(0,10))
        restart_btn = tk.Button(right_frame, text="Restart", command=self.restart)
        restart_btn.pack(fill="x")
        quit_btn = tk.Button(right_frame, text="Quit", command=self.root.quit)
        quit_btn.pack(fill="x", pady=(6,0))

    def on_cell_click(self, index):
        if self.field.field[index].is_empty():
            moved = self.field.move(index, self.current_player)
            if moved:
                filled = self.field.played_moves()[index]
                self.buttons[index].config(text=filled)
                result = self.brains.check_winner(self.field)
                if result in ("X", "O"):
                    self._disable_all_buttons()
                    self.status_var.set(f"Player {result} wins!")
                    messagebox.showinfo("Game Over", f"Player {result} wins!")
                elif result == "draw":
                    self._disable_all_buttons()
                    self.status_var.set("It's a draw!")
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    self._switch_player()
                    self._update_status()
        else:
            messagebox.showwarning("Invalid move", "Cell already occupied.")

    def _switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def _update_status(self):
        self.status_var.set(f"Player {self.current_player}'s turn")

    def _disable_all_buttons(self):
        for b in self.buttons:
            b.config(state="disabled")

    def restart(self):
        self.field.reset_field()
        for b in self.buttons:
            b.config(text="", state="normal")
        self.current_player = "X"
        self._update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
