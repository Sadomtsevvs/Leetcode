import time
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        max = 0
        result = None
        counter = defaultdict(int)
        for i in range(1, len(nums)):
            if nums[i-1] != key:
                continue
            counter[nums[i]] += 1
            if counter[nums[i]] > max:
                max = counter[nums[i]]
                result = nums[i]
        return result


# _nums = [2,2,2,2,3]
# _key = 2
_nums = [1,100,200,1,100]
_key = 1

print(Solution().mostFrequent(_nums, _key))
