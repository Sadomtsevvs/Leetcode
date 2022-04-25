from time import time


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_pos = ''
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_pos == '':
                    zero_pos = i
            elif zero_pos != '':
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1

        ''' another solution
        filled = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[filled] = nums[i]
                filled += 1
        for i in range(filled, len(nums)):
            nums[i] = 0
        '''


start_time = time()

_nums = [0, 1, 0, 3, 12]

Solution().moveZeroes(_nums)

print(_nums)

print("--- %s seconds ---" % (time() - start_time))
