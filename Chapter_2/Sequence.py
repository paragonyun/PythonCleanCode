from collections.abc import Sequence


class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        self._values[item] = "바꼈지롱"
        return self._values[item]


item = Items(1, 2, 3)
print(item[2])
