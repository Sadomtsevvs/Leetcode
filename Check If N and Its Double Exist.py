from time import time


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 1):
            itwo = arr[i] * 2
            ihalf = arr[i] / 2
            for j in range(i + 1, len(arr)):
                if arr[j] == itwo or arr[j] == ihalf:
                    return True
        return False


start_time = time()

_arr = [10, 2, 5, 3]

print(Solution().checkIfExist(_arr))

print("--- %s seconds ---" % (time() - start_time))
