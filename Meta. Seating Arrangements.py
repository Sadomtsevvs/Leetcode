from time import time
from heapq import *


class Solution:
    def minOverallAwkwardness(self, arr):
        heap = [-a for a in arr]
        heapify(heap)
        guest1 = - heappop(heap)
        guest2 = - heappop(heap)
        ans = guest1 - guest2
        while heap:
            new_guest = - heappop(heap)
            if guest1 >= guest2:
                ans = max(ans, guest1 - new_guest)
                guest1 = new_guest
            else:
                ans = max(ans, guest2 - new_guest)
                guest2 = new_guest
        return max(ans, abs(guest1 - guest2))


start_time = time()

_arr = [5, 10, 6, 8]
_arr = [4, 4, 5, 5, 6]
# n = 4
# arr = [5, 10, 6, 8]
# output = 4
# If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table
# (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent guests
# will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4,
# yielding an overall awkwardness of 4. It's impossible to achieve a smaller overall awkwardness.

print(Solution().minOverallAwkwardness(_arr))

print("--- %s seconds ---" % (time() - start_time))
