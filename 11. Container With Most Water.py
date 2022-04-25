from time import time


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # brute force solution
        #
        # size = len(height)
        # result = 0
        # max_left = 0
        # for left in range(0, size - 1):
        #     if left > 0 and height[left] <= max_left:
        #         continue
        #     max_left = height[left]
        #     max_right = 0
        #     for right in reversed(range(left + 1, size)):
        #         if right < (size - 1) and height[right] <= max_right:
        #             continue
        #         if left > 0 and height[left - 1] >= height[right]:
        #             continue
        #         max_right = height[right]
        #         area = min(height[left], height[right]) * (right - left)
        #         result = max(result, area)
        #         if height[right] >= height[left]:
        #             break
        # return result

        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result


start_time = time()

_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution().maxArea(_height))

print("--- %s seconds ---" % (time() - start_time))
