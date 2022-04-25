from time import time


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1

        # from LC comments
        # 
        # the count of odd numbers between 1 and low - 1 is low / 2
        # the count of odd numbers between 1 and high is (high + 1 ) / 2

        # return (high + 1) / 2 - low / 2

start_time = time()

_low = 3
_high = 7
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

print(Solution().countOdds(_low, _high))

print("--- %s seconds ---" % (time() - start_time))
