import unittest
from Multiset import Multiset


class TestMultiset(unittest.TestCase):

    # --- Проверка comb_check ---
    def test_comb_check_valid_empty(self):
        self.assertTrue(Multiset("{}").comb_check())

    def test_comb_check_invalid_unbalanced(self):
        self.assertFalse(Multiset("{{a}").comb_check())

    def test_comb_check_valid_nested(self):
        self.assertTrue(Multiset("{{a,b},c}").comb_check())

    # --- Проверка parse() ---
    def test_parse_simple(self):
        m = Multiset("{a,b,a}")
        self.assertEqual(m.dict, {"a": 2, "b": 1})

    def test_parse_nested(self):
        m = Multiset("{{a,b},{a,b},c}")
        keys = list(m.dict.keys())
        self.assertTrue(any(isinstance(k, tuple) for k in keys))
        self.assertIn("c", m.dict)

    def test_parse_invalid_returns_empty(self):
        m = Multiset("{,}")
        self.assertEqual(m.parse(), {})

    # --- string_to_dict ---
    def test_string_to_dict_mixed(self):
        m = Multiset("{}")
        data = ["a", "{b,c}", "a"]
        result = m.string_to_dict(data)
        self.assertIn("a", result)
        nested_key = [k for k in result if isinstance(k, tuple)]
        self.assertTrue(len(nested_key) > 0)

    # --- _format_key и output ---
    def test_format_key_simple(self):
        m = Multiset("{a}")
        self.assertEqual(m._format_key("a"), "a")

    def test_format_key_nested(self):
        inner = Multiset("{a,b}")
        key = tuple(sorted(inner.dict.items()))
        m = Multiset("{{a,b}}")
        s = m._format_key(key)
        self.assertIn("{", s)

    def test_output_prints(self):
        m = Multiset("{a,a,b}")
        m.output()  # просто проверяем, что не вызывает ошибок

    # --- edit() ---
    def test_edit_valid(self):
        m = Multiset("{a}")
        m.edit(new_string="{a,b}")
        self.assertIn("b", m.dict)

    def test_edit_invalid(self):
        m = Multiset("{a}")
        m.edit(new_string="{,}")
        self.assertIn("a", m.dict)

    def test_edit_registry_valid(self):
        m = Multiset("{a}")
        reg = {"1": m}
        m.edit(new_string="{a,b}", registry=reg, key="1")
        self.assertIn("b", reg["1"].dict)

    def test_edit_registry_missing_key(self):
        m = Multiset("{a}")
        reg = {}
        m.edit(new_string="{a,b}", registry=reg, key="2")
        # просто проверяем, что не падает

    def test_edit_none_string(self):
        m = Multiset("{a}")
        m.edit(new_string=None)
        self.assertIn("a", m.dict)

    # --- power и contains ---
    def test_power_contains(self):
        m = Multiset("{a,a,b}")
        self.assertEqual(m.power(), 3)
        self.assertTrue(m.contains("a"))
        self.assertFalse(m.contains("z"))

    # --- операции ---
    def test_union(self):
        m1 = Multiset("{a,b}")
        m2 = Multiset("{b,c}")
        u = m1.union(m2)
        self.assertEqual(u.dict["b"], 2)
        self.assertIn("a", u.dict)
        self.assertIn("c", u.dict)

    def test_intersection(self):
        m1 = Multiset("{a,a,b}")
        m2 = Multiset("{a,b,b}")
        inter = m1.intersection(m2)
        self.assertEqual(inter.dict["a"], 1)
        self.assertEqual(inter.dict["b"], 1)

    def test_difference(self):
        m1 = Multiset("{a,a,b}")
        m2 = Multiset("{a}")
        diff = m1.difference(m2)
        self.assertEqual(diff.dict["a"], 1)
        self.assertIn("b", diff.dict)


if __name__ == "__main__":
    unittest.main()
