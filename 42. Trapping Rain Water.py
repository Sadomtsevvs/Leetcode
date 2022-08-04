from time import time
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        # third solution
        #
        # result = 0
        # water_l_r = []
        # max_h = 0
        # for h in height:
        #     max_h = max(max_h, h)
        #     water_l_r.append(max_h - h)
        # max_h = 0
        # for i in range(len(height)-1, -1, -1):
        #     h = height[i]
        #     max_h = max(max_h, h)
        #     result += min(water_l_r[i], max_h - h)
        # return result

        # second solution, after reading official
        #
        result = 0
        left, right = 0, len(height) - 1
        height_left = 0
        height_right = 0
        while left < right:
            if height[left] <= height[right]:
                height_left = max(height_left, height[left])
                result += (height_left - height[left])
                left += 1
            else:
                height_right = max(height_right, height[right])
                result += (height_right - height[right])
                right -= 1
        return result

        # my first solution: here I first fill the water between two borders,
        # and then subtract it if I find the wall on its place
        #
        # result = 0
        # left, right = 0, len(height) - 1
        # cur_height = 0
        # move_left = False
        # move_right = False
        # while left < right:
        #     if move_left:
        #         result -= min(cur_height, height[left])
        #     if move_right:
        #         result -= min(cur_height, height[right])
        #     new_height = max(cur_height, min(height[left], height[right]))
        #     result += (new_height-cur_height) * (right - left - 1)
        #     cur_height = new_height
        #     if height[left] <= height[right]:
        #         left += 1
        #         move_left = True
        #         move_right = False
        #     else:
        #         right -= 1
        #         move_left = False
        #         move_right = True
        # return result

        # from LC
        #
        # left = 0
        # right = len(height) - 1
        #
        # left_max = 0
        # right_max = 0
        # ans = 0
        #
        # while left < right:
        #     if height[left] < height[right]:
        #         if height[left] >= left_max:
        #             left_max = height[left]
        #         else:
        #             ans += left_max - height[left]
        #         left += 1
        #     else:
        #         if height[right] >= right_max:
        #             right_max = height[right]
        #         else:
        #             ans += right_max - height[right]
        #         right -= 1
        # return ans


start_time = time()

_height = [0,1,0,2,1,0,1,3,2,1,2,1]
_height = [4,2,0,3,2,5]
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

print(Solution().trap(_height))

print("--- %s seconds ---" % (time() - start_time))