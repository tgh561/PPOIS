from Field import Field

class Brains:
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    @staticmethod
    def check_winner(field: Field):
        state = field.played_moves()
        for a, b, c in Brains.winning_combinations:
            if state[a] == state[b] == state[c] and state[a] is not None:
                return state[a]
        if all(cell is not None for cell in state):
            return "draw"
        return None
