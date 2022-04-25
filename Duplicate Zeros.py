from time import time


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        new_arr = []
        for i in arr:
            new_arr.append(i)
            if i == 0:
                new_arr.append(i)
        arr[:] = new_arr[:len(arr)]


start_time = time()

_arr = [1, 0, 2, 3, 0, 4, 5, 0]

Solution().duplicateZeros(_arr)
print(_arr)

print("--- %s seconds ---" % (time() - start_time))
