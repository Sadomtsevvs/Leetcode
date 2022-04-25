from time import time


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:

        if len(nums) == 1:
            return

        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= prev:
                prev = nums[i]
            else:
                min_max = 101
                j_min_max = 0
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        min_max = min(min_max, nums[j])
                        j_min_max = j
                nums[i], nums[j_min_max] = nums[j_min_max], nums[i]
                # nums[:] = nums[:i+1] + sorted(nums[i+1:])
                nums[:] = nums[:i+1] + nums[i+1:][::-1]
                break
        else:
            nums.sort()


start_time = time()

_nums = [2,4,3,1]

# Input: nums = [1,2,3]
# Output: [1,3,2]

Solution().nextPermutation(_nums)
print(_nums)

print("--- %s seconds ---" % (time() - start_time))
