from time import time


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:

        d = dict()
        result = 0
        cur_result = 0
        beg = 0
        for i in range(len(nums)):
            if nums[i] in d:
                ind_i = d[nums[i]]
                while ind_i >= beg:
                    cur_result -= nums[beg]
                    beg += 1
            d[nums[i]] = i
            cur_result += nums[i]
            result = max(result, cur_result)
        return result


        # amount = 0
        # cur_amount = 0
        # cur_dict = {}
        # begin = 0
        # for i in range(len(nums)):
        #     pos = cur_dict.get(nums[i])
        #     if pos is not None:
        #         amount = max(amount, cur_amount)
        #         for j in range(begin, pos + 1):
        #             cur_dict.pop(nums[j])
        #             cur_amount -= nums[j]
        #         begin = pos + 1
        #     cur_dict[nums[i]] = i
        #     cur_amount += nums[i]
        # return max(amount, cur_amount)

        # Babichev
        #
        # beg, end, S, n, sm = 0, 0, set(), len(nums), 0
        # ans = 0
        # while end < n:
        #     if nums[end] not in S:
        #         sm += nums[end]
        #         S.add(nums[end])
        #         end += 1
        #         ans = max(ans, sm)
        #     else:
        #         sm -= nums[beg]
        #         S.remove(nums[beg])
        #         beg += 1
        # return ans



_nums = [4,2,4,5,6]
_nums = [5,2,1,2,5,2,1,2,5]
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

start_time = time()

print(Solution().maximumUniqueSubarray(_nums))

print("--- %s seconds ---" % (time() - start_time))