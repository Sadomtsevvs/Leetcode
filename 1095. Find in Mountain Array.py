from time import time

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: list) -> int:
        # find peak
        peak, ipeak = 0, 0
        beg, end = 0, len(mountain_arr) - 1
        while beg < end:
            i2 = (end + beg) // 2
            i1 = i2 - 1
            i3 = i2 + 1
            val1 = mountain_arr[i1]
            val2 = mountain_arr[i2]
            val3 = mountain_arr[i3]
            if val1 < val2 > val3:
                if val1 == target:
                    return i1
                if val2 == target:
                    return i2
                peak = val2
                ipeak = i2
                break
            elif val1 < val2 < val3:
                if val1 == target:
                    return i1
                if val2 == target:
                    return i2
                if val3 == target:
                    return i3
                beg = i2
            else:
                end = i2
        if peak < target:
            return -1
        beg, end = 0, ipeak - 1
        while beg <= end:
            med = (end + beg) // 2
            val = mountain_arr[med]
            if val == target:
                return med
            elif val < target:
                beg = med + 1
            else:
                end = med - 1
        beg, end = ipeak + 1, len(mountain_arr) - 1
        while beg <= end:
            med = (end + beg) // 2
            val = mountain_arr[med]
            if val == target:
                return med
            elif val < target:
                end = med - 1
            else:
                beg = med + 1
        return -1




start_time = time()

# Example 1:
# Input: array = [1,2,3,4,5,3,1], target = 3
# _array = [1,2,3,4,5,3,1]
# _target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
#
# Example 2:
# Input: array = [0,1,2,4,2,1], target = 3
# _array = [0,1,2,4,2,1]
# _target = 5
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
_array = [1,5,2]
_target = 1

print(Solution().findInMountainArray(_target, _array))

print("--- %s seconds ---" % (time() - start_time))