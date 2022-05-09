from time import time


class Solution:
    def balancedSplitExists(self, arr):
        arr.sort()
        left, right = -1, len(arr)
        sum_left, sum_right = 0, 0
        while left < right - 1:
            if sum_left <= sum_right:
                left += 1
                sum_left += arr[left]
            else:
                right -= 1
                sum_right += arr[right]
        return sum_right == sum_left and arr[left] < arr[right]


start_time = time()

_arr = [12, 7, 6, 7, 6]
# _arr = [1, 5, 7, 1]
# arr = [12, 7, 6, 7, 6]
# output = false
# We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement
# that all integers in A are smaller than all integers in B.

print(Solution().balancedSplitExists(_arr))

print("--- %s seconds ---" % (time() - start_time))
