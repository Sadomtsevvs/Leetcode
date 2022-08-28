class LinkedList:

    def __init__(self, val):
        self.val = val
        self.next = None


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.cur_size = 0
        self.cur_sum = 0
        self.head = None
        self.tail = None

    def next(self, val: int) -> float:
        if not self.head:
            self.head = LinkedList(val)
            self.tail = self.head
        else:
            self.tail.next = LinkedList(val)
            self.tail = self.tail.next
        self.cur_size += 1
        self.cur_sum += val
        if self.cur_size > self.size:
            self.cur_size -= 1
            self.cur_sum -= self.head.val
            self.head = self.head.next
        return self.cur_sum / min(self.size, self.cur_size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)