from time import time


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # result = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             result += 1
        # return result

        # great, but i don't understand
        #
        ans, n = 0, len(nums)
        preSum = 0
        dic = {0: 1}
        for num in nums:
            preSum += num
            if preSum - k in dic:
                ans += dic[preSum - k]
            dic[preSum] = dic.get(preSum, 0) + 1
        return ans


start_time = time()

_nums = [1,2,3]
_k = 3
# Input: nums = [1,2,3], k = 3
# Output: 2
_nums = [0,1,-1,-1,-1,2,0]
_k = -1

print(Solution().subarraySum(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
