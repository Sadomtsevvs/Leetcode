from time import time


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l, r, l1 = 0, len(nums) - 1, None
        while l < r:
            if nums[l] == 0:
                if l1 is None:
                    l += 1
                else:
                    nums[l], nums[l1] = nums[l1], nums[l]
                    l1 += 1
            elif nums[r] == 2:
                r -= 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            elif nums[r] == 0:
                if l1 is None:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                else:
                    nums[l1], nums[r] = nums[r], nums[l1]
                    l1 += 1
            elif l1 is None:
                l1 = l
                l += 1
            else:
                l += 1

        # from LC comments, elegant
        # https: // en.wikipedia.org / wiki / Dutch_national_flag_problem
        #
        # beg, mid, end = 0, 0, len(nums) - 1
        #
        # while mid <= end:
        #     if nums[mid] == 0:
        #         nums[beg], nums[mid] = nums[mid], nums[beg]
        #         mid += 1
        #         beg += 1
        #     elif nums[mid] == 2:
        #         nums[mid], nums[end] = nums[end], nums[mid]
        #         end -= 1
        #     else:  # nums[mid] == 1:
        #         mid += 1


start_time = time()

_nums = [2,0,2,1,1,0]
_nums = [2,0,2,1,0,2,0,1,1,1,2,1,0]
# _nums = [1,2,2,2,2,0,0,0,1,1]
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

Solution().sortColors(_nums)
print(_nums)

print("--- %s seconds ---" % (time() - start_time))
