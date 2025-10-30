class Cell:
    def __init__(self, filled=None):
        self.__filled = filled

    @property
    def filled(self):
        return self.__filled

    @filled.setter
    def filled(self, move):
        if self.__filled is not None:
            print(f"Already filled with {self.__filled}")
            return
        if move is None:
            return
        # Accept both letter O and digit 0 as O
        m = str(move).upper()
        if m == "0":
            m = "O"
        if m in ("X", "O"):
            self.__filled = m
        else:
            print("Invalid move. Use X or O.")

    def reset(self):
        self.__filled = None

    def is_empty(self):
        return self.__filled is None
