from time import time


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        amount = 0
        cur_amount = 0
        cur_dict = {}
        begin = 0
        for i in range(len(nums)):
            pos = cur_dict.get(nums[i])
            if pos is not None:
                amount = max(amount, cur_amount)
                for j in range(begin, pos + 1):
                    cur_dict.pop(nums[j])
                    cur_amount -= nums[j]
                begin = pos + 1
            cur_dict[nums[i]] = i
            cur_amount += nums[i]
        return max(amount, cur_amount)


data = list(map(int, input().split(',')))
# data = [5,2,1,2,5,2,1,2,5]

start_time = time()

print(Solution().maximumUniqueSubarray(data))

print("--- %s seconds ---" % (time() - start_time))