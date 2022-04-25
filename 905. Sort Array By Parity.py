from time import time


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        pos_odd = None
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if pos_odd is not None:
                    nums[i], nums[pos_odd] = nums[pos_odd], nums[i]
                    pos_odd += 1
            else:
                if pos_odd is None:
                    pos_odd = i
        return nums

        # nice solution from LC comments
        #
        # front = 0
        # back = len(nums) - 1
        # while front < back:
        #     if nums[front] % 2 == 0:
        #         front += 1
        #     elif nums[back] % 2 == 1:
        #         back -= 1
        #     else:
        #         temp = nums[front]
        #         nums[front] = nums[back]
        #         nums[back] = temp
        # return nums

start_time = time()

_nums = [3,1,2,5,4,7,8,1]
# _nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

print(Solution().sortArrayByParity(_nums))

print("--- %s seconds ---" % (time() - start_time))
