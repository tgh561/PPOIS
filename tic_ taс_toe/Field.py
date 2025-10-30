from Cell import Cell

class Field:
    def __init__(self):
        self.field = [Cell() for _ in range(9)]

    def move(self, index: int, move: str) -> bool:
        if not (0 <= index < 9):
            return False
        cell = self.field[index]
        if cell.is_empty():
            cell.filled = move
            return True
        else:
            return False

    def reset_field(self):
        for i in range(9):
            self.field[i].reset()

    def played_moves(self):
        return [cell.filled for cell in self.field]
