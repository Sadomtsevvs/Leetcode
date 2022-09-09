class LinkedList:
    def __init__(self, time, hits=0):
        self.time = time
        self.hits = hits
        self.next = None


class HitCounter:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sum = 0

    def hit(self, timestamp: int) -> None:
        if not self.head:
            self.head = LinkedList(timestamp, 1)
            self.tail = self.head
        elif self.tail.time == timestamp:
            self.tail.hits += 1
        else:
            self.tail.next = LinkedList(timestamp, 1)
            self.tail = self.tail.next
        self.sum += 1

    def getHits(self, timestamp: int) -> int:
        while self.head and self.head.time <= timestamp - 300:
            self.sum -= self.head.hits
            self.head = self.head.next
        return self.sum

# soluton from LC, deque
#
# class HitCounter(object):
#
#     def __init__(self):
#         self.counter = deque()
#
#     def hit(self, timestamp):
#         self.counter.append(timestamp)
#
#     def getHits(self, timestamp):
#         while self.counter and timestamp -self.counter[0] >= 300:
#             self.counter.popleft()
#         return len(self.counter)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)