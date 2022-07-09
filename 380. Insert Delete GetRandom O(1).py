from random import randint


class RandomizedSet:

    def __init__(self):
        self.val_num = dict()
        self.num_val = dict()
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.val_num:
            return False
        self.length += 1
        self.val_num[val] = self.length
        self.num_val[self.length] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_num:
            return False
        num = self.val_num[val]
        if num != self.length:
            last = self.num_val[self.length]
            self.val_num[last] = num
            self.num_val[num] = last
        del self.val_num[val]
        del self.num_val[self.length]
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return self.num_val[randint(1, self.length)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()