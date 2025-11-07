import unittest
from Field import Field
from Brains import Brains

class TestBrains(unittest.TestCase):
    def make_field(self, vals):
        f = Field()
        for idx, val in enumerate(vals):
            if val is not None:
                f.move(idx, val)
        return f

    def test_all_winning_combinations(self):
        wins = [
            ["X", "X", "X", None, None, None, None, None, None],
            [None, None, None, "O", "O", "O", None, None, None],
            [None, None, None, None, None, None, "X", "X", "X"],
            ["X", None, None, "X", None, None, "X", None, None],
            [None, "O", None, None, "O", None, None, "O", None],
            [None, None, "X", None, None, "X", None, None, "X"],
            ["X", None, None, None, "X", None, None, None, "X"],
            [None, None, "O", None, "O", None, "O", None, None],
        ]
        for vals in wins:
            f = self.make_field(vals)
            self.assertIn(Brains.check_winner(f), ("X", "O"))

    def test_detects_draw(self):
        vals = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        f = self.make_field(vals)
        self.assertEqual(Brains.check_winner(f), "draw")

    def test_returns_none_for_ongoing_game(self):
        vals = ["X", "O", None, None, None, None, None, None, None]
        f = self.make_field(vals)
        self.assertIsNone(Brains.check_winner(f))

    def test_sequence_leads_to_win(self):
        f = Field()
        self.assertTrue(f.move(0, "X"))
        self.assertTrue(f.move(1, "X"))
        self.assertTrue(f.move(2, "X"))
        self.assertEqual(Brains.check_winner(f), "X")
