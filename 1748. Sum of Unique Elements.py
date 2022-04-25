from time import time


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        res = 0
        seen = set()
        seen_twice = set()
        for num in nums:
            if num in seen_twice:
                continue
            if num in seen:
                res -= num
                seen_twice.add(num)
            else:
                res += num
                seen.add(num)
        return res

        # from Lee
        #
        # return sum(a for a, c in collections.Counter(A).items() if c == 1)

start_time = time()

_nums = [1,2,3,2]
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

print(Solution().sumOfUnique(_nums))

print("--- %s seconds ---" % (time() - start_time))
