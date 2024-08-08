class MyHashSet:

    def __init__(self):
        # 0 <= key <= 10**6 --> size is then 1000001
        self.set = [False] * 1000001

    def add(self, key: int) -> None:
        # set true because it is filled
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)