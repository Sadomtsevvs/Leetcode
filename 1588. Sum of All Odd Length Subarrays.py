from time import time


class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:

        # brute force
        ans = 0
        for i in range(len(arr)):
            cur_sum = 0
            for j in range(i, len(arr)):
                cur_sum += arr[j]
                if (j - i) % 2 == 0:
                    ans += cur_sum
        return ans

        # from LC comments
        #
        # def sumOddLengthSubarrays(self, A):
        #     res, n = 0, len(A)
        #     for i, a in enumerate(A):
        #         res += ((i + 1) * (n - i) + 1) / 2 * a
        #     return res
        #
        # def sumOddLengthSubarrays(self, A):
        #     return sum(((i + 1) * (len(A) - i) + 1) / 2 * a for i, a in enumerate(A))
        #
        # res = 0; freq = 0; n = len(arr)
        # for i in range(n):
        #     freq = freq-(i+1)//2+(n-i+1)//2
        #     res += freq*arr[i]
        # return res


start_time = time()

_arr = [1,4,2,5,3]
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

print(Solution().sumOddLengthSubarrays(_arr))

print("--- %s seconds ---" % (time() - start_time))
