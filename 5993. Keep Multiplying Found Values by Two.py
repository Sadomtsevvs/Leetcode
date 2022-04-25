from time import time


class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        find_mult = set()
        for num in nums:
            if num % original == 0:
                find_mult.add(num // original)
        for i in range(len(find_mult)):
            if 2**i in find_mult:
                original *= 2
            else:
                break
        return original



start_time = time()

_nums = [5,3,61,12]
_original = 3
# Input: nums = [5,3,6,1,12], original = 3
# Output: 24
# Explanation:
# - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
# - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
# - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
# - 24 is not found in nums. Thus, 24 is returned.

print(Solution().findFinalValue(_nums, _original))

print("--- %s seconds ---" % (time() - start_time))