from time import time


class Solution:
    def findPositions(self, arr, x):
        result = []
        ind = 0
        k = x
        while k > 0:
            val_max = -1
            ind_max = -1
            for _ in range(min(x, len(arr) + k - x)):
                while arr[ind] == -1:
                    ind = (ind+1) % len(arr)
                if arr[ind] > val_max:
                    val_max = arr[ind]
                    ind_max = ind
                if arr[ind] > 0:
                    arr[ind] -= 1
                ind = (ind+1) % len(arr)
            result.append(ind_max+1)
            arr[ind_max] = -1
            k -= 1
        return result



start_time = time()

_arr = [1, 2, 2, 3, 4, 5]
_x = 5
# _arr = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
# _x = [2, 5, 10, 13]
# Example
# n = 6
# arr = [1, 2, 2, 3, 4, 5]
# x = 5
# output = [5, 6, 4, 1, 2]
# The initial queue is [1, 2, 2, 3, 4, 5] (from front to back).
# In the first iteration, the first 5 elements are popped off the queue, leaving just [5]. Of the popped elements, the largest one is the 4, which was at index 5 in the original array. The remaining elements are then decremented and added back onto the queue, whose contents are then [5, 0, 1, 1, 2].
# In the second iteration, all 5 elements are popped off the queue. The largest one is the 5, which was at index 6 in the original array. The remaining elements are then decremented (aside from the 0) and added back onto the queue, whose contents are then [0, 0, 0, 1].
# In the third iteration, all 4 elements are popped off the queue. The largest one is the 1, which had the initial value of 3 at index 4 in the original array. The remaining elements are added back onto the queue, whose contents are then [0, 0, 0].
# In the fourth iteration, all 3 elements are popped off the queue. Since they all have an equal value, we remove the one that was popped first, which had the initial value of 1 at index 1 in the original array. The remaining elements are added back onto the queue, whose contents are then [0, 0].
# In the final iteration, both elements are popped off the queue. We remove the one that was popped first, which had the initial value of 2 at index 2 in the original array.

print(Solution().findPositions(_arr, _x))

print("--- %s seconds ---" % (time() - start_time))
