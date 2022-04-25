from time import time
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        return [mc[0] for mc in Counter(nums).most_common(k)]

        # official solution
        #
        # # O(1) time
        # if k == len(nums):
        #     return nums
        #
        # # 1. build hash map : character and how often it appears
        # # O(N) time
        # count = Counter(nums)
        # # 2-3. build heap of top k frequent elements and
        # # convert it into an output array
        # # O(N log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get)

        # O(n) solution from LC comments
        # the idea is to make list, where indexes equals frequency and values are values
        #
        # bucket = [[] for _ in range(len(nums) + 1)]
        # Count = Counter(nums).items()
        # for num, freq in Count:
        #     bucket[freq].append(num)
        # flat_list = [item for sublist in bucket for item in sublist]
        # return flat_list[::-1][:k]


start_time = time()

_nums = [3,1,1,1,1,2,2]
_k = 2
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

print(Solution().topKFrequent(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
