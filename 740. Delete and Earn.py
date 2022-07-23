from time import time
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:

        dict_num = defaultdict(int)
        for num in nums:
            dict_num[num] += num

        result = [0] * (max(dict_num) + 1)
        result[0] = dict_num[0]
        result[1] = max(dict_num[0], dict_num[1])
        for i in range(2, max(dict_num) + 1):
            result[i] = max(result[i-1], result[i-2] + dict_num[i])
        return result[max(dict_num)]

        # my second solution, TLE
        # dic = defaultdict(int)
        # for num in nums:
        #     dic[num] += num
        #
        # def dp(free):
        #     result = 0
        #     for key in free:
        #         result = max(result, dic[key] + dp(free - {key, key - 1, key + 1}))
        #     return result
        #
        # return dp(set(nums))

        # my first solution, wrong
        # Input [3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10]
        # Output 65
        # Expected 66

        # result = 0
        # dict_num = defaultdict(int)
        # for num in nums:
        #     dict_num[num] += num
        # while len(dict_num) > 0:
        #     max_value = - float('inf')
        #     num_to_delete = -1
        #     for num in dict_num:
        #         num_value = dict_num[num]
        #         if dict_num.get(num-1):
        #             num_value -= dict_num[num-1]
        #         if dict_num.get(num+1):
        #             num_value -= dict_num[num+1]
        #         if num_value > max_value:
        #             num_to_delete = num
        #             max_value = num_value
        #     result += dict_num[num_to_delete]
        #     dict_num.pop(num_to_delete)
        #     if dict_num.get(num_to_delete - 1):
        #         dict_num.pop(num_to_delete - 1)
        #     if dict_num.get(num_to_delete + 1):
        #         dict_num.pop(num_to_delete + 1)
        # return result


start_time = time()

# _nums = [3,7,10,5,2,4,8,9,9,4,9,2,6,4,6,5,4,7,6,10]
_nums = [2,2,3,3,3,4]
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.

print(Solution().deleteAndEarn(_nums))

print("--- %s seconds ---" % (time() - start_time))
