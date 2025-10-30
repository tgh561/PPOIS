##
# @file multiset.py
# @brief Implementation of Multiset class for handling nested multisets
#

class Multiset:
    ##
    # @brief Constructor
    #
    def __init__(self, string):
        self.string = string
        self.dict = {}
        self.parse()

    ##
    # @brief Validates the multiset string
    #
    def comb_check(self):
        if self.string == "{}":
            return True
        if self.string.count("{") != self.string.count("}"):
            return False
        if not self.string.startswith("{") or not self.string.endswith("}"):
            return False
        invalid_combinations = [",,", "{,}", ",}", ", {", "{ ,", " , "]
        for combo in invalid_combinations:
            if combo in self.string:
                return False
        if len(self.string) > 2:
            inner = self.string[1:-1]
            if inner.endswith(",") or inner.startswith(","):
                return False
        for char in self.string:
            if char not in "{}," and not char.isalnum() and char != " ":
                return False
        return True

    ##
    # @brief Parses the input string into dictionary
    #
    def parse(self):
        self.dict = {}
        if not self.comb_check():
            print("Invalid input!")
            return self.dict

        parsed_string = []
        current = ""
        level = 0
        for ch in self.string[1:-1]:
            if ch == "{":
                level += 1
                current += ch
            elif ch == "}":
                level -= 1
                current += ch
            elif ch == "," and level == 0:
                parsed_string.append(current.strip())
                current = ""
            else:
                current += ch
        if current:
            parsed_string.append(current.strip())

        return self.string_to_dict(parsed_string)

    ##
    # @brief Converts parsed string list to dict
    #
    def string_to_dict(self, string_to_parse):
        for item in string_to_parse:
            item = item.strip()
            if not item:
                continue
            if item.startswith("{") and item.endswith("}"):
                nested = Multiset(item).parse()
                key = tuple(sorted(nested.items(), key=lambda kv: str(kv[0])))
                self.dict[key] = self.dict.get(key, 0) + 1
            else:
                self.dict[item] = self.dict.get(item, 0) + 1
        return self.dict

    ##
    # @brief Formats dictionary key for output
    #
    def _format_key(self, key):
        if isinstance(key, tuple) and all(isinstance(el, tuple) and len(el) == 2 for el in key):
            parts = []
            for k, v in key:
                k_str = self._format_key(k) if isinstance(k, tuple) else str(k)
                parts.append(f"{k_str}: {v}")
            return "{" + ", ".join(parts) + "}"
        if isinstance(key, tuple):
            return "(" + ", ".join(self._format_key(k) if isinstance(k, tuple) else str(k) for k in key) + ")"
        return str(key)

    ##
    # @brief Prints formatted multiset
    #
    def output(self):
        if not self.dict:
            print("{}")
            return
        parts = [f"{self._format_key(k)}: {v}" for k, v in self.dict.items()]
        print(", ".join(parts))

    ##
    # @brief Edits multiset string and updates dict
    #
    def edit(self, new_string=None, registry=None, key=None):
        target = self
        if registry is not None and key is not None:
            if key not in registry:
                print(f"Нет мультимножества с номером {key}")
                return
            target = registry[key]

        if new_string is None:
            print("Пустая строка. Редактирование отменено.")
            return

        old_dict = target.dict.copy()
        target.string = new_string
        if target.comb_check():
            target.parse()
            target.output()
        else:
            print("Некорректный ввод.")
            target.dict = old_dict  # возвращаем исходное

    ##
    # @brief Calculates power (sum of counts)
    #
    def power(self):
        return sum(self.dict.values())

    ##
    # @brief Checks if element exists
    #
    def contains(self, element):
        return element in self.dict

    ##
    # @brief Union of multisets
    #
    def union(self, other):
        result = Multiset("{}")
        for key in set(self.dict.keys()).union(other.dict.keys()):
            result.dict[key] = self.dict.get(key, 0) + other.dict.get(key, 0)
        return result

    ##
    # @brief Intersection of multisets
    #
    def intersection(self, other):
        result = Multiset("{}")
        for key in set(self.dict.keys()).intersection(other.dict.keys()):
            result.dict[key] = min(self.dict[key], other.dict[key])
        return result

    ##
    # @brief Difference of multisets
    #
    def difference(self, other):
        result = Multiset("{}")
        for key in self.dict:
            count = self.dict[key] - other.dict.get(key, 0)
            if count > 0:
                result.dict[key] = count
        return result
