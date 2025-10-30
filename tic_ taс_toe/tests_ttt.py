import unittest
from unittest import mock
from io import StringIO

from Cell import Cell
from Field import Field
from Brains import Brains

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()

    def test_initial_state(self):
        self.assertIsNone(self.cell.filled)
        self.assertTrue(self.cell.is_empty())

    def test_accepts_and_normalizes_moves(self):
        cases = [("x","X"),("X","X"),("o","O"),("O","O"),("0","O"),(0,"O")]
        for inp, expected in cases:
            with self.subTest(inp=inp):
                c = Cell()
                c.filled = inp
                self.assertEqual(c.filled, expected)
                self.assertFalse(c.is_empty())

    def test_invalid_move_prints_message_and_keeps_none(self):
        c = Cell()
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            c.filled = "Z"
            out = fake_out.getvalue()
        self.assertTrue(out.strip() != "" and "Invalid move" in out or out.strip() != "")
        self.assertIsNone(c.filled)

    def test_cannot_overwrite_existing_value(self):
        c = Cell()
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            c.filled = "X"
            c.filled = "O"
            out = fake_out.getvalue()
        self.assertIn("Already filled", out)
        self.assertEqual(c.filled, "X")

    def test_reset_clears_value(self):
        c = Cell()
        c.filled = "X"
        self.assertEqual(c.filled, "X")
        c.reset()
        self.assertIsNone(c.filled)
        self.assertTrue(c.is_empty())

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field()

    def test_initial_board_empty(self):
        moves = self.field.played_moves()
        self.assertIsInstance(moves, list)
        self.assertEqual(len(moves), 9)
        self.assertTrue(all(x is None for x in moves))

    def test_move_valid_updates_played_moves(self):
        ok = self.field.move(0, "X")
        self.assertTrue(ok)
        self.assertEqual(self.field.played_moves()[0], "X")
        ok2 = self.field.move(1, "0")
        self.assertTrue(ok2)
        self.assertEqual(self.field.played_moves()[1], "O")

    def test_move_out_of_bounds_returns_false(self):
        self.assertFalse(self.field.move(-1, "X"))
        self.assertFalse(self.field.move(9, "X"))

    def test_move_on_occupied_cell_returns_false(self):
        self.assertTrue(self.field.move(4, "X"))
        self.assertFalse(self.field.move(4, "O"))
        self.assertEqual(self.field.played_moves()[4], "X")

    def test_reset_field_clears_all(self):
        for i in range(9):
            self.field.move(i, "X" if i % 2 == 0 else "O")
        self.assertTrue(all(v in ("X","O") for v in self.field.played_moves()))
        self.field.reset_field()
        self.assertTrue(all(v is None for v in self.field.played_moves()))

class TestBrains(unittest.TestCase):
    def make_field(self, values):
        f = Field()
        for idx, val in enumerate(values):
            if val is not None:
                f.move(idx, val)
        return f

    def test_all_winning_combinations(self):
        cases = [
            (["X","X","X", None,None,None, None,None,None], "X"),
            ([None,None,None, "O","O","O", None,None,None], "O"),
            ([None,None,None, None,None,None, "X","X","X"], "X"),
            (["X",None,None, "X",None,None, "X",None,None], "X"),
            ([None,"O",None, None,"O",None, None,"O",None], "O"),
            ([None,None,"X", None,None,"X", None,None,"X"], "X"),
            (["X",None,None, None,"X",None, None,None,"X"], "X"),
            ([None,None,"O", None,"O",None, "O",None,None], "O"),
        ]
        for vals, expected in cases:
            with self.subTest(vals=vals):
                f = self.make_field(vals)
                self.assertEqual(Brains.check_winner(f), expected)

    def test_detects_draw(self):
        vals = ["X","O","X","X","O","O","O","X","X"]
        f = self.make_field(vals)
        self.assertEqual(Brains.check_winner(f), "draw")

    def test_returns_none_for_ongoing_game(self):
        vals = [None,"X",None, None,None,None, None,None,None]
        f = self.make_field(vals)
        self.assertIsNone(Brains.check_winner(f))

class TestIntegrationSequence(unittest.TestCase):
    def test_sequence_leads_to_win(self):
        f = Field()
        self.assertTrue(f.move(0, "X"))
        self.assertIsNone(Brains.check_winner(f))
        self.assertTrue(f.move(1, "O"))
        self.assertTrue(f.move(4, "X"))
        self.assertIsNone(Brains.check_winner(f))
        self.assertTrue(f.move(2, "O"))
        self.assertTrue(f.move(8, "X"))
        self.assertEqual(Brains.check_winner(f), "X")

if __name__ == "__main__":
    unittest.main()
