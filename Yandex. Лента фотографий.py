from math import ceil
from time import time


class Solution:
    def foto(self):
        w = int(input())
        n, k = map(int, input().split(' '))
        heights = []
        for i in range(n):
            ww, hh = map(int, input().split('x'))
            heights.append(ceil(hh * w / ww))
        heights.sort()
        min_h = 0
        max_h = 0
        for i in range(k):
            min_h += heights[i]
            max_h += heights[-i-1]
        print(min_h)
        print(max_h)


start_time = time()

Solution().foto()

print("--- %s seconds ---" % (time() - start_time))
