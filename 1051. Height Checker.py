from time import time


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        original = heights[:]
        for i in range(len(heights) - 1):
            change_happened = False
            min = i
            for j in range(i, len(heights) - 1):
                if heights[j] > heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    change_happened = True
                if heights[j] < heights[min]:
                    min = j
            if not change_happened:
                break
            if i != min:
                heights[i], heights[min] = heights[min], heights[i]
        result = 0
        for i in range(len(heights)):
            if heights[i] != original[i]:
                result += 1
        return result

        # from LC comments. They used built-in function sorted()!!!
        #
        # sorted_height = sorted(heights)
        # counter = 0
        # for i in range(0, len(heights)):
        #     if sorted_height[i] != heights[i]:
        #         counter += 1
        # return counter

start_time = time()

_heights = [7,3,5,5,1,2,2,3,9,2,2,7,1,7,3,2,3,6,6,7]
# _heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

print(Solution().heightChecker(_heights))

print("--- %s seconds ---" % (time() - start_time))
