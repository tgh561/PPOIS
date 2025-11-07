class Multiset:
    def __init__(self, string):
        self.string = string
        self.dict = {}
        self.parse()

    def сomb_check(self):
        if self.string == "{}":
            return True
        if self.string.count("{") != self.string.count("}"):
            return False
        if not self.string.startswith("{") or not self.string.endswith("}"):
            return False
        invalid_combinations = [",,", "{,}", ",}", " , "]
        for combo in invalid_combinations:
            if combo in self.string:
                return False
        if len(self.string) > 2:
            if self.string[1:-1][-1] == "," or self.string[1:-1][0] == ",":
                return False
        for char in self.string:
            if char not in "{}," and not char.isalnum() and char != " ":
                return False
        return True

    def parse(self):
        self.dict = {}
        if not self.сomb_check():
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

    def _format_key(self, key):
        if isinstance(key, tuple) and all(isinstance(el, tuple) and len(el) == 2 for el in key):
            parts = []
            for k, v in key:
                if isinstance(k, tuple):
                    k_str = self._format_key(k)
                else:
                    k_str = str(k)
                parts.append(f"{k_str}: {v}")
            return "{" + ", ".join(parts) + "}"
        if isinstance(key, tuple):
            return "(" + ", ".join(self._format_key(k) if isinstance(k, tuple) else str(k) for k in key) + ")"
        return str(key)

    def output(self):
        parts = []
        for key, count in self.dict.items():
            parts.append(f"{self._format_key(key)}: {count}")
        print(", ".join(parts))

    def edit(self, new_string=None, registry=None, key=None):
        target = self
        if registry is not None and key is not None:
            if key not in registry:
                print(f"Нет мультимножества с номером {key}")
                return
            target = registry[key]
        while True:
            if new_string is None:
                new_string = input("Введите новую строку мультимножества: ").strip()
            target.string = new_string
            if target.сomb_check():
                target.parse()
                target.output()
                return
            print("Некорректный ввод. Попробуйте ещё раз.")
            new_string = None

    def power(self):
        return sum(self.dict.values())

    def contains(self, element):
        return element in self.dict

    def union(self, other):
        result = Multiset("{}")
        for key in set(self.dict.keys()).union(other.dict.keys()):
            result.dict[key] = self.dict.get(key, 0) + other.dict.get(key, 0)
        return result

    def intersection(self, other):
        result = Multiset("{}")
        for key in set(self.dict.keys()).intersection(other.dict.keys()):
            result.dict[key] = min(self.dict[key], other.dict[key])
        return result

    def difference(self, other):
        result = Multiset("{}")
        for key in self.dict:
            count = self.dict[key] - other.dict.get(key, 0)
            if count > 0:
                result.dict[key] = count
        return result
