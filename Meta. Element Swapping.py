from time import time


class Solution:
    def findMinArray(self, arr, k):
        moves_remain = k
        start = 0
        while moves_remain > 0 and start < len(arr) - 1:
            minel = arr[start]
            minind = start
            for i in range(1, moves_remain + 1):
                if i + start > len(arr) - 1:
                    break
                if arr[i+start] < minel:
                    minel = arr[i+start]
                    minind = i + start
            if minind != start:
                for i in range(minind, start, - 1):
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                moves_remain -= (minind - start)
            start += 1
        return arr


start_time = time()

_arr = [5, 3, 1]
_k = 1

_arr = [1, 2, 3, 4, 1]
_k = 2

# n = 3
# k = 2
# arr = [5, 3, 1]
# output = [1, 5, 3]
# We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3].
# This is the lexicographically smallest sequence achievable after at most 2 swaps.

# n = 5
# k = 3
# arr = [8, 9, 11, 2, 1]
# output = [2, 8, 9, 11, 1]
# We can swap [11, 2], followed by [9, 2], then [8, 2].

print(Solution().findMinArray(_arr, _k))

print("--- %s seconds ---" % (time() - start_time))
