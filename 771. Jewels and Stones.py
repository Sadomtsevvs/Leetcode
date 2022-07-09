from time import time


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        ans = 0
        for stone in stones:
            if stone in jewels:
                ans += 1
        return ans

        # another solution
        #
        # return sum(s in set(jewels) for s in stones)


start_time = time()

_jewels = "aA"
_stones = "aAAbbbb"
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Input: jewels = "z", stones = "ZZ"
# Output: 0

print(Solution().numJewelsInStones(_jewels, _stones))

print("--- %s seconds ---" % (time() - start_time))