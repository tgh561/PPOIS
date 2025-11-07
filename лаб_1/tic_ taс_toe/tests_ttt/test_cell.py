import unittest
from Cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()

    def test_initial_state_empty(self):
        self.assertTrue(self.cell.is_empty())
        self.assertIsNone(self.cell.filled)

    def test_fill_with_X(self):
        self.cell.filled = "X"
        self.assertEqual(self.cell.filled, "X")

    def test_fill_with_O(self):
        self.cell.filled = "O"
        self.assertEqual(self.cell.filled, "O")

    def test_fill_twice_does_not_change(self):
        self.cell.filled = "X"
        self.cell.filled = "O"
        self.assertEqual(self.cell.filled, "X")

    def test_reset_makes_empty(self):
        self.cell.filled = "X"
        self.cell.reset()
        self.assertTrue(self.cell.is_empty())
