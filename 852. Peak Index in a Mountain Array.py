from time import time


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 1, len(arr) - 2
        while True:
            mid = (right + left) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] < arr[mid]:
                left = mid + 1
            else:
                right = mid


start_time = time()

_arr = [0,13,11,10,2]
# Input: arr = [0,10,5,2]
# Output: 1

print(Solution().peakIndexInMountainArray(_arr))

print("--- %s seconds ---" % (time() - start_time))
