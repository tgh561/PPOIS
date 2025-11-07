import unittest
from Field import Field

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field()

    def test_field_has_9_cells(self):
        self.assertEqual(len(self.field.field), 9)

    def test_move_valid_updates_cell(self):
        ok = self.field.move(0, "X")
        self.assertTrue(ok)
        self.assertEqual(self.field.played_moves()[0], "X")

    def test_move_on_occupied_cell_returns_false(self):
        self.assertTrue(self.field.move(4, "X"))
        self.assertFalse(self.field.move(4, "O"))

    def test_move_out_of_bounds_returns_false(self):
        self.assertFalse(self.field.move(-1, "X"))
        self.assertFalse(self.field.move(9, "O"))

    def test_reset_field_clears_all(self):
        for i in range(9):
            self.field.move(i, "X" if i % 2 == 0 else "O")
        self.field.reset_field()
        self.assertTrue(all(m is None for m in self.field.played_moves()))
