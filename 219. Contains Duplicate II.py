from time import time


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_positions = {}
        for i in range(len(nums)):
            if nums[i] in last_positions and i - last_positions[nums[i]] <= k:
                return True
            else:
                last_positions[nums[i]] = i
        return False

        # from LC comments
        #
        # dic = {}
        # for i, v in enumerate(nums):
        #     if v in dic and i - dic[v] <= k:
        #         return True
        #     dic[v] = i
        # return False


start_time = time()

_nums = [1, 2, 3, 1]
_k = 3
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.

print(Solution().containsNearbyDuplicate(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
