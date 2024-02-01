import random


class RandomizedSet:
    def __init__(self):
        self._values = []
        self._hash = {}

    def insert(self, val: int) -> bool:
        if val in self._hash:
            return False
        self._values.append(val)
        self._hash[val] = len(self._values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._hash:
            return False
        val_pos = self._hash.get(val)
        if val_pos + 1 != len(self._values):
            last_pos = len(self._values) - 1
            self._values[val_pos] = self._values[last_pos]
            self._hash[self._values[val_pos]] = val_pos
        del self._values[-1]
        self._hash.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self._values)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(15)
obj.insert(21)
obj.remove(15)
print(obj.getRandom())
