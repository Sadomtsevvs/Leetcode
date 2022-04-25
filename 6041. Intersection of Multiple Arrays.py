from time import time


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        ans = set(nums[0])
        for num in nums:
            ans = ans.intersection(set(num))
        return sorted(list(ans))


start_time = time()

_nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation:
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

print(Solution().intersection(_nums))

print("--- %s seconds ---" % (time() - start_time))