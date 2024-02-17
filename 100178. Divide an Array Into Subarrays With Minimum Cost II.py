from functools import cache
from time import time
from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:

        n = len(nums)
        sl = SortedList(nums[1 : 1 + dist])
        cursum, minsum = sum(sl[: k - 2]), float('inf')
        for i in range(1 + dist, n):
            if sl.bisect(nums[i]) <= k - 2:
                cursum += nums[i]
            else:
                cursum += sl[k - 2]
            minsum = min(minsum, cursum)
            sl.add(nums[i])
            if sl.bisect(nums[i - dist]) <= k - 2:
                cursum -= nums[i - dist]
            else:
                cursum -= sl[k - 2]
            sl.remove(nums[i - dist])
        return nums[0] + minsum


        # my solution
        #
        # @cache
        # def dp(i, left_parts, start):
        #     if i >= len(nums):
        #         return float('inf')
        #     result = nums[i]
        #     if left_parts == 1:
        #         return result
        #     part = k - left_parts + 1
        #     if part == 2:
        #         start = i
        #     result_next = float('inf')
        #     for end in range(i, len(nums)-1):
        #         next_start = end + 1
        #         if part >= 2 and next_start - start > dist:
        #             break
        #         if left_parts - 1 > len(nums) - next_start:
        #             break
        #         result_next = min(result_next, dp(next_start, left_parts - 1, start))
        #     return result + result_next
        #
        # return dp(0, k, 0)


start_time = time()

# Example 1:
# Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
_nums = [1,3,2,6,4,2]
_k = 3
_dist = 3
# Output: 5
# Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
#
# Example 2:
# Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
# _nums = [10,1,2,2,2,1]
# _k = 4
# _dist = 3
# Output: 15
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
# The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
#
# Example 3:
# Input: nums = [10,8,18,9], k = 3, dist = 1
_nums = [10,8,18,9]
_k = 3
_dist = 1
# Output: 36
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
# The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.

# _nums = [4,14,3,6,10,7,26,45,29,14,8,5,31,39,25,6,46,28,8,29,20,29,16,24,27,23,11,43,37,47]
# _k = 27
# _dist = 27

# _nums = [102087,344542,53910,450247,155477,434227,181687,393356,64907,425963,385166,459356,201295,93036,367154,489679,
#          94684,472107,366654,206861,105439,118141,87643,462569,290793,376659,393907,479187,412518,417697,87018,42496,
#          139021,127115,107882,455848,58141,342522,218522,82282,328936,442554,476905,266823,366020,31138,46899,274882,
#          351823,416713,312473,45094,44491,384275,356448,150181,252660,331125,336578,103842,25561,111303,164370,283353,
#          380451,131215,350689,64821,110078,37242,255996,125110,398166,87773,439412,450169,14153,420759,52321,360896,
#          475821,145046,226994,438025,165748,376634,211101,17658,482066,186667,447111,468028,373107,174447,408878,422318,
#          452928,344927,6466,410081]
# _k = 82
# _dist = 94

# _nums = [486312,464288,242795,374900,125348,50327,413208,432373,456380,142800,36896,240917,90770,409649,293663,51188,
#          395857,193222,92756,11764,240599,64641,447655,430847,492437,318775,60402,309466,484502,80255,48147,116086,
#          44588,195399,174819,393654,388274,235999,245739,109815,71777,401494,243779,392687,233550,162279,475900,75481,
#          465754,332769,176423,338260,392654,390757,485824,255846,345145,410751,59469,286367,469178,79512,361444,211983,
#          404004,6976,278577,126780,39252,81070,35804,449470,148385,95411,390669,77785,209961,252400,136066,374072,
#          201932,105143,198155,404905,130428,336525,380792,247717,498122,304775,78693,274685,208717,217315,114042,27593,
#          420091,292260,378732,146467]
# _k = 48
# _dist = 68

print(Solution().minimumCost(_nums, _k, _dist))

print("--- %s seconds ---" % (time() - start_time))
