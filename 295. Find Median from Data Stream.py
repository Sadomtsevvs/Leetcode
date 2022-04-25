from time import time
from heapq import *


class MedianFinder:

    def __init__(self):
        heapmin, heapmax = [], []
        heapify(heapmin)
        heapify(heapmax)
        self.heapmin = heapmin
        self.heapmax = heapmax

    def addNum(self, num: int) -> None:
        if len(self.heapmin) == 0 and len(self.heapmax) == 0:
            heappush(self.heapmin, num)
        elif len(self.heapmin) > len(self.heapmax):
            if num >= self.heapmin[0]:
                heappush(self.heapmax, - heapreplace(self.heapmin, num))
            else:
                heappush(self.heapmax, - num)
        elif len(self.heapmin) < len(self.heapmax):
            if num <= -self.heapmax[0]:
                heappush(self.heapmin, - heapreplace(self.heapmax, - num))
            else:
                heappush(self.heapmin, num)
        else:
            if num >= self.heapmin[0]:
                heappush(self.heapmin, num)
            else:
                heappush(self.heapmax, - num)

    def findMedian(self) -> float:
        if len(self.heapmin) > len(self.heapmax):
            return self.heapmin[0]
        if len(self.heapmin) < len(self.heapmax):
            return - self.heapmax[0]
        return (self.heapmin[0] - self.heapmax[0]) / 2


start_time = time()

medianFinder = MedianFinder();
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
medianFinder.addNum(4)
print(medianFinder.findMedian())
medianFinder.addNum(0)
print(medianFinder.findMedian())
medianFinder.addNum(0)
print(medianFinder.findMedian())
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian();

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

print("--- %s seconds ---" % (time() - start_time))
