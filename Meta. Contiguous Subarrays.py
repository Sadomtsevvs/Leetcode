from time import time


class Solution:
    def count_subarrays(self, arr):
        left_bourders = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if not stack:
                left_bourders[i] = -1
            else:
                left_bourders[i] = stack[-1]
            stack.append(i)
        left_halfves = [i - left_bourders[i] for i in range(len(arr))]

        right_bourders = [0] * len(arr)
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if not stack:
                right_bourders[i] = len(arr)
            else:
                right_bourders[i] = stack[-1]
            stack.append(i)
        right_halfves = [right_bourders[i] - i for i in range(len(arr))]
        return [left_halfves[i] + right_halfves[i] - 1 for i in range(len(arr))]


start_time = time()

_arr = [3, 4, 1, 6, 2]
_arr = [3, 1, 2, 1, 2, 6, 2]
# arr = [3, 4, 1, 6, 2]
# output = [1, 3, 1, 5, 1]
# Explanation:
# For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
# For index 1 - [4], [3, 4], [4, 1]
# For index 2 - [1]
# For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
# For index 4 - [2]
# So, the answer for the above input is [1, 3, 1, 5, 1]

print(Solution().count_subarrays(_arr))

print("--- %s seconds ---" % (time() - start_time))
