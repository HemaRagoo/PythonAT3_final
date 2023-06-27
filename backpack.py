class BackPack:
    def __init__(self):
        self._backpack = []

    def list(self):
        return [item.name for item in self._backpack]

    def add(self, item):
        if item is not None:
            self._backpack.append(item)

    def remove(self, item_name):
        item = next(
            (item for item in self._backpack if item.name.lower() == item_name.lower()), None)
        if item:
            self._backpack.remove(item)

    def count(self):
        return len(self._backpack)

    def in_backpack(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self._backpack)

    def _binary_search(self, item_name, start, end):
        if start > end:
            return False

        mid = (start + end) // 2
        mid_item_name = self._backpack[mid].name.lower()

        if mid_item_name == item_name:
            return True
        elif mid_item_name < item_name:
            return self._binary_search(item_name, mid + 1, end)
        else:
            return self._binary_search(item_name, start, mid - 1)
