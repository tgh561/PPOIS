class Brains:
    @staticmethod
    def check_winner(field):
        moves = field.played_moves()

        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for line in lines:
            a, b, c = line
            if moves[a] and moves[a] == moves[b] == moves[c]:
                return moves[a]

        if all(m is not None for m in moves):
            return "draw"

        return None
