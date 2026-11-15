class MyHashSet:

    def __init__(self):
        self.hashset = [-1]*10000000
        

    def add(self, key: int) -> None:
        self.hashset[key] = key
        

    def remove(self, key: int) -> None:
        self.hashset[key] = -1
        

    def contains(self, key: int) -> bool:
        if self.hashset[key] == -1:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)