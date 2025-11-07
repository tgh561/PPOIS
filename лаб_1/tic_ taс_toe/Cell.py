class Cell:
    def __init__(self):
        self._filled = None

    @property
    def filled(self):
        return self._filled

    @filled.setter
    def filled(self, value):
        if self._filled is not None:
            print("Already filled")
            return

        if value is None:
            self._filled = None
            return

        # нормализуем вход
        v = str(value).upper()
        if v in ["X"]:
            self._filled = "X"
        elif v in ["O", "0", "О"]:  # поддержка нуля и русской О
            self._filled = "O"
        else:
            print("Invalid move")
            self._filled = None

    def is_empty(self):
        return self._filled is None

    def reset(self):
        self._filled = None
