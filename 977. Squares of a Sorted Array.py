from time import time


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        if nums[0] >= 0:
            left_index = 0
            right_index = 0
        elif nums[-1] < 0:
            left_index = len_nums - 1
            right_index = len_nums - 1
        else:
            for ind in range(1, len_nums):
                if nums[ind - 1] < 0 and nums[ind] >= 0:
                    left_index = ind - 1
                    right_index = ind
                    break
        result = []
        while left_index >= 0 or right_index < len_nums:
            if left_index == right_index:
                result.append(nums[left_index] ** 2)
                left_index -= 1
                right_index += 1
            elif left_index >= 0 and right_index < len_nums:
                if abs(nums[left_index]) < abs(nums[right_index]):
                    result.append(nums[left_index]**2)
                    left_index -= 1
                else:
                    result.append(nums[right_index]**2)
                    right_index += 1
            elif left_index >= 0:
                result.append(nums[left_index]**2)
                left_index -= 1
            else:
                result.append(nums[right_index]**2)
                right_index += 1
        return result


start_time = time()

_nums = [0, 2]

print(Solution().sortedSquares(_nums))

print("--- %s seconds ---" % (time() - start_time))
