from Cell import Cell

class Field:
    def __init__(self):
        self.field = [Cell() for _ in range(9)]

    def move(self, index, move):
        if index < 0 or index >= len(self.field):
            print("Invalid cell index")
            return False
        cell = self.field[index]
        if not cell.is_empty():
            print("Already filled")
            return False
        cell.filled = move
        return True

    def reset_field(self):
        for cell in self.field:
            cell.reset()

    def played_moves(self):
        return [cell.filled for cell in self.field]
