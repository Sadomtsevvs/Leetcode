from time import time
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # after reading official
        #
        nums.sort()
        diff = float('inf')
        for i in range(len(nums) - 2):
            sum1 = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum3 = sum1 + nums[left] + nums[right]
                if abs(target - sum3) < abs(diff):
                    diff = target - sum3
                if sum3 < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break
        return target - diff

        # wrong logic, case _nums = [4,0,5,-5,3,-4]
        #
        # diff = float('inf')
        # ans = nums[0] + nums[1] + nums[2]
        #
        # nums.sort()
        # left, right = 0, len(nums) - 1
        # while left < right - 1:
        #     sum2 = nums[left] + nums[right]
        #     left_i, right_i = left + 1, right - 1
        #     while left_i <= right_i:
        #         sum3 = sum2 + nums[left_i]
        #         if abs(sum3 - target) < diff:
        #             diff = abs(sum3 - target)
        #             ans = sum3
        #         if sum3 > target:
        #             right -= 1
        #             break
        #         sum3 = sum2 + nums[right_i]
        #         if abs(sum3 - target) < diff:
        #             diff = abs(sum3 - target)
        #             ans = sum3
        #         if sum3 < target:
        #             left += 1
        #             break
        #         # left_i += 1
        #         right_i -= 1
        #     else:
        #         # left += 1
        #         right -= 1
        # return ans

        # Brute force O(n**3)
        #
        # diff = float('inf')
        # ans = nums[0] + nums[1] + nums[2]
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j+1, len(nums)):
        #             s = nums[i] + nums[j] + nums[k]
        #             if abs(s - target) < diff:
        #                 diff = abs(s - target)
        #                 ans = s
        # return ans


start_time = time()


_nums = [-1, 2, 1, -4]
_target = 1
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0

_nums = [40,-53,36,89,-38,-51,80,11,-10,76,-30,46,-39,-15,4,72,83,-25,33,-69,-73,-100,-23,-37,-13,-62,-26,-54,36,-84,
         -65,-51,11,98,-21,49,51,78,-58,-40,95,-81,41,-17,-70,83,-88,-14,-75,-10,-44,-21,6,68,-81,-1,41,-61,-82,-24,45,
         19,6,-98,11,9,-66,50,-97,-2,58,17,51,-13,88,-16,-77,31,35,98,-2,0,-70,6,-34,-8,78,22,-1,-93,-39,-88,-77,-65,80,
         91,35,-15,7,-37,-96,65,3,33,-22,60,1,76,-32,22]
_target = 292
# Expected 291

_nums = [13,252,-87,-431,-148,387,-290,572,-311,-721,222,673,538,919,483,-128,-518,7,-36,-840,233,-184,-541,522,-162,
         127,-935,-397,761,903,-217,543,906,-503,-826,-342,599,-726,960,-235,436,-91,-511,-793,-658,-143,-524,-609,-728,
         -734,273,-19,-10,630,-294,-453,149,-581,-405,984,154,-968,623,-631,384,-825,308,779,-7,617,221,394,151,-282,
         472,332,-5,-509,611,-116,113,672,-497,-182,307,-592,925,766,-62,237,-8,789,318,-314,-792,-632,-781,375,939,
         -304,-149,544,-742,663,484,802,616,501,-269,-458,-763,-950,-390,-816,683,-219,381,478,-129,602,-931,128,502,
         508,-565,-243,-695,-943,-987,-692,346,-13,-225,-740,-441,-112,658,855,-531,542,839,795,-664,404,-844,-164,-709,
         167,953,-941,-848,211,-75,792,-208,569,-647,-714,-76,-603,-852,-665,-897,-627,123,-177,-35,-519,-241,-711,-74,
         420,-2,-101,715,708,256,-307,466,-602,-636,990,857,70,590,-4,610,-151,196,-981,385,-689,-617,827,360,-959,-289,
         620,933,-522,597,-667,-882,524,181,-854,275,-600,453,-942,134]
_target = -2805
# Expected -2805

# _nums = [0,1,2]
# _target = 3


_nums = [4,0,5,-5,3,-4]
_target = -2
# Expected -2

print(Solution().threeSumClosest(_nums, _target))

print("--- %s seconds ---" % (time() - start_time))
