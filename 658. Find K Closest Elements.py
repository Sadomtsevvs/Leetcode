from time import time
import heapq


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:

        if len(arr) == k:
            return arr

        # first find the closest index to the x
        l, r = 0, len(arr) - 1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            arr_mid = arr[mid]
            if arr_mid == x:
                break
            if arr_mid < x:
                l = mid + 1
            else:
                r = mid

        # two pointers
        l = mid if mid == 0 else mid - 1
        r = mid + 1 if mid == 0 else mid
        heap = []
        heapq.heapify(heap)
        while len(heap) < k:
            if l < 0:
                heapq.heappush(heap, arr[r])
                r += 1
            elif r > len(arr) - 1:
                heapq.heappush(heap, arr[l])
                l -= 1
            else:
                modl = abs(arr[l] - x)
                modr = abs(arr[r] - x)
                if modl > modr:
                    heapq.heappush(heap, arr[r])
                    r += 1
                else:
                    heapq.heappush(heap, arr[l])
                    l -= 1
        return [heapq.heappop(heap) for _ in range(k)]

        # amazing solution from LC comment
        #
        # left, right = 0, len(arr) - k
        # while left < right:
        #     mid = (left + right) / 2
        #     if x - arr[mid] > arr[mid + k] - x:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return arr[left:left + k]


start_time = time()

_arr = [1,2,3,4,5]
_k = 4
_x = -1

_arr = [1,2]
_k = 1
_x = 9

_arr = [1,1,2,2,2,2,2,3,3]
_x = 3
_k = 3

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

print(Solution().findClosestElements(_arr, _k, _x))

print("--- %s seconds ---" % (time() - start_time))
