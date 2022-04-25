from time import time


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # result = 0
        # maxx = 0
        # for num in nums:
        #     result ^= num
        #     maxx = max(maxx, num)
        # return abs(maxx - result) if maxx != result else maxx

        # official solution
        #
        # slow, fast = nums[0], nums[0]
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        # slow = nums[0]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow

        # binary search solution
        #
        # 'low' and 'high' represent the range of values of the target
        # low = 1
        # high = len(nums) - 1
        #
        # while low <= high:
        #     cur = (low + high) // 2
        #     count = 0
        #
        #     # Count how many numbers are less than or equal to 'cur'
        #     count = sum(num <= cur for num in nums)
        #     if count > cur:
        #         duplicate = cur
        #         high = cur - 1
        #     else:
        #         low = cur + 1
        #
        # return duplicate

        beg, end = 1, len(nums) - 1

        while beg + 1 <= end:
            mid, count = (beg + end) // 2, 0
            for num in nums:
                if num <= mid: count += 1
            if count <= mid:
                beg = mid + 1
            else:
                end = mid
        return end


start_time = time()

_nums = [3,1,1,4,2]
# _nums = [1,3,4,2,2]
# _nums = [1,1,2]
# _nums = [1,2,3,3,3,3,4]
# Input: nums = [3,1,3,4,2]
# Output: 3

print(Solution().findDuplicate(_nums))

print("--- %s seconds ---" % (time() - start_time))
