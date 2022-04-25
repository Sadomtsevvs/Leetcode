from time import time


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        vacant_ind = None
        for i in range(len(nums)):
            if nums[i] == val:
                if vacant_ind is None:
                    vacant_ind = i
            else:
                k += 1
                if vacant_ind is not None:
                    nums[i], nums[vacant_ind] = nums[vacant_ind], nums[i]
                    vacant_ind += 1
        return k

        """ better solution from LC
        k = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[k] = nums[i]
                k +=1
        return k         
        """

start_time = time()

_nums = [0, 1, 2, 2, 3, 0, 4, 2]
_val = 2

Solution().removeElement(_nums, _val)
print(_nums)

print("--- %s seconds ---" % (time() - start_time))