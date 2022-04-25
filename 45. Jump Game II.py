from time import time


class Solution:
    def jump(self, nums: list[int]) -> int:

        # # this solution is very slow, O(n^2)
        # result = [float("inf")] * len(nums)
        # result[0] = 0
        # for i in range(len(nums) - 1):
        #     for j in range(1, nums[i] + 1):
        #         if i + j > len(nums) - 1:
        #             break
        #         result[i+j] = min(result[i+j], result[i] + 1)
        # return result[-1]

        result = [0] * len(nums)
        left_min = 1
        for i in range(len(nums) - 1):
            for j in range(left_min, i + nums[i] + 1):
                if j > len(nums) - 1:
                    break
                result[j] = result[i] + 1
                left_min += 1
        return result[-1]


start_time = time()

_nums = [1, 1, 2, 1, 4]
# Output: 2


print(Solution().jump(_nums))

print("--- %s seconds ---" % (time() - start_time))
