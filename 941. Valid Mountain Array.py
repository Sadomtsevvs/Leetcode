from time import time


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        direct = None
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if direct is None:
                if arr[i] < arr[i - 1]:
                    return False
                elif arr[i] > arr[i - 1]:
                    direct = True
            elif direct:
                if arr[i] < arr[i - 1]:
                    direct = False
            elif arr[i] > arr[i - 1]:
                return False
        return direct is False


start_time = time()

_arr = [2, 1, 2, 3, 2]

print(Solution().validMountainArray(_arr))

print("--- %s seconds ---" % (time() - start_time))
