from time import time


class Solution:
    def getTotalTime(self, arr):
        arr.sort()
        ans = 0
        a1 = arr.pop()
        while arr:
            a2 = arr.pop()
            s = a1 = a1 + a2
            ans += s
        return ans


start_time = time()

_arr = [4, 2, 1, 3]
# Example
# arr = [4, 2, 1, 3]
# output = 26
# First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
# Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
# Add 9 + 1 for a penalty of 10. The penalties sum to 26.

print(Solution().getTotalTime(_arr))

print("--- %s seconds ---" % (time() - start_time))
