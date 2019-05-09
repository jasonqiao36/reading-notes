class Average:
    def __init__(self):
        self._items = []

    def __call__(self, new_value):
        self._items.append(new_value)
        return sum(self._items) / len(self._items)
