import unittest
from unittest.mock import patch
from Multiset import Multiset  # предполагается, что твой файл называется multiset.py


class TestMultiset(unittest.TestCase):

    # ====== Проверка сomb_check ======
    def test_comb_check_valid_empty(self):
        m = Multiset("{}")
        self.assertTrue(m.сomb_check())

    def test_comb_check_unbalanced_braces(self):
        m = Multiset("{{}")
        self.assertFalse(m.сomb_check())

    def test_comb_check_invalid_structure(self):
        m = Multiset("{,}")
        self.assertFalse(m.сomb_check())

    def test_comb_check_invalid_chars(self):
        m = Multiset("{a@b}")
        self.assertFalse(m.сomb_check())

    def test_comb_check_extra_commas(self):
        m = Multiset("{a,,b}")
        self.assertFalse(m.сomb_check())

    def test_comb_check_trailing_comma(self):
        m = Multiset("{a,}")
        self.assertFalse(m.сomb_check())

    def test_comb_check_leading_comma(self):
        m = Multiset("{,a}")
        self.assertFalse(m.сomb_check())

    def test_comb_check_valid_complex(self):
        m = Multiset("{a,b,c}")
        self.assertTrue(m.сomb_check())

    # ====== Проверка parse ======
    def test_parse_invalid_prints_message(self):
        with patch("builtins.print") as mock_print:
            m = Multiset("{,}")
            m.parse()
            mock_print.assert_any_call("Invalid input!")

    def test_parse_simple(self):
        m = Multiset("{a,b,a}")
        expected = {"a": 2, "b": 1}
        self.assertEqual(m.dict, expected)

    def test_parse_nested(self):
        m = Multiset("{{a,b},{a,b}}")
        # внутри два одинаковых множества {a,b}
        self.assertEqual(len(m.dict), 1)
        key = list(m.dict.keys())[0]
        self.assertIn(('a', 1), key)
        self.assertEqual(m.dict[key], 2)

    def test_parse_empty_inner(self):
        m = Multiset("{{}}")
        key = list(m.dict.keys())[0]
        self.assertEqual(m.dict[key], 1)

    # ====== Проверка string_to_dict ======
    def test_string_to_dict_mixed(self):
        m = Multiset("{}")
        result = m.string_to_dict(["a", "{b}", "{b}"])
        self.assertEqual(result["a"], 1)
        nested_key = [k for k in result if isinstance(k, tuple)][0]
        self.assertEqual(result[nested_key], 2)

    # ====== Проверка _format_key ======
    def test_format_key_simple(self):
        m = Multiset("{}")
        self.assertEqual(m._format_key("a"), "a")

    def test_format_key_tuple(self):
        m = Multiset("{}")
        self.assertEqual(m._format_key(("a", "b")), "(a, b)")

    def test_format_key_nested_dict(self):
        m = Multiset("{}")
        nested = ((('a', 1), ('b', 2)),)
        formatted = m._format_key(nested)
        # проверяем, что оба ключа и значения присутствуют
        self.assertIn("a", formatted)
        self.assertIn("1", formatted)
        self.assertIn("b", formatted)
        self.assertIn("2", formatted)


    # ====== Проверка output ======
    def test_output_prints(self):
        m = Multiset("{a,a}")
        with patch("builtins.print") as mock_print:
            m.output()
            mock_print.assert_called()

    # ====== Проверка edit ======
    def test_edit_with_valid_input(self):
        m = Multiset("{a}")
        with patch("builtins.input", return_value="{b}"), patch("builtins.print"):
            m.edit()
        self.assertIn("b", m.dict)

    def test_edit_with_invalid_then_valid(self):
        m = Multiset("{a}")
        with patch("builtins.input", side_effect=["{,}", "{c}"]), patch("builtins.print"):
            m.edit()
        self.assertIn("c", m.dict)

    def test_edit_with_registry(self):
        m1 = Multiset("{a}")
        m2 = Multiset("{b}")
        registry = {1: m1}
        with patch("builtins.print"):
            m2.edit("{c}", registry, 1)
        self.assertIn("c", registry[1].dict)

    def test_edit_with_registry_invalid_key(self):
        m1 = Multiset("{a}")
        registry = {}
        with patch("builtins.print") as mock_print:
            m1.edit("{b}", registry, 5)
            mock_print.assert_any_call("Нет мультимножества с номером 5")

    # ====== Проверка power, contains ======
    def test_power(self):
        m = Multiset("{a,a,b}")
        self.assertEqual(m.power(), 3)

    def test_contains(self):
        m = Multiset("{x,y}")
        self.assertTrue(m.contains("x"))
        self.assertFalse(m.contains("z"))

    # ====== Проверка union, intersection, difference ======
    def test_union(self):
        m1 = Multiset("{a,a,b}")
        m2 = Multiset("{a,c}")
        result = m1.union(m2)
        self.assertEqual(result.dict["a"], 3)
        self.assertEqual(result.dict["b"], 1)
        self.assertEqual(result.dict["c"], 1)

    def test_intersection(self):
        m1 = Multiset("{a,a,b}")
        m2 = Multiset("{a,b,b}")
        result = m1.intersection(m2)
        self.assertEqual(result.dict["a"], 1)
        self.assertEqual(result.dict["b"], 1)

    def test_difference(self):
        m1 = Multiset("{a,a,b}")
        m2 = Multiset("{a,b,b}")
        result = m1.difference(m2)
        self.assertEqual(result.dict, {"a": 1})

    def test_difference_all_removed(self):
        m1 = Multiset("{a}")
        m2 = Multiset("{a}")
        result = m1.difference(m2)
        self.assertEqual(result.dict, {})


if __name__ == "__main__":
    unittest.main()
