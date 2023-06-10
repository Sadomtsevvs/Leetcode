import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.maximum = 1
        self.heap = []
        self.set_heap = set()

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.set_heap.remove(num)
        else:
            num = self.maximum
            self.maximum += 1
        return num

    def addBack(self, num: int) -> None:
        if num >= self.maximum:
            return
        if num in self.set_heap:
            return
        heapq.heappush(self.heap, num)
        self.set_heap.add(num)