from collections import defaultdict
from time import time
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # O(n*k), where k = indexDiff, TLE
        #
        # start = 0
        # for i in range(1, len(nums)):
        #     if i - start > indexDiff:
        #         start += 1
        #     num = nums[i]
        #     for j in range(start, i):
        #         if abs(num - nums[j]) <= valueDiff:
        #             return True
        # return False

        dic = defaultdict(list)
        for i, num in enumerate(nums):
            if dic[num] and i - dic[num][-1] <= indexDiff:
                return True
            dic[num].append(i)
        nums_sort = sorted(list(set(nums)))
        for i in range(len(nums_sort) - 1):
            f = nums_sort[i]
            first_idxs = dic[f]
            second_idxs = []
            j = i + 1
            while j < len(nums_sort) and nums_sort[j] - f <= valueDiff:
                second_idxs += dic[nums_sort[j]]
                j += 1
            if not second_idxs:
                continue
            # two pointers search
            second_idxs.sort()
            first = 0
            second = 0
            while first < len(first_idxs) and second < len(second_idxs):
                if abs(second_idxs[second] - first_idxs[first]) <= indexDiff:
                    return True
                if first_idxs[first] < second_idxs[second]:
                    first += 1
                else:
                    second += 1
        return False

        # solution from Babichev
        #
        # SList = SortedList()
        # for i in range(len(nums)):
        #     if i > k:SList.remove(nums[i - k - 1])
        #     pos1 = SortedList.bisect_left(SList, nums[i] - t)
        #     pos2 = SortedList.bisect_right(SList, nums[i] + t)
        #
        #     if pos1 != pos2 and pos1 != len(SList): return True
        #
        #     SList.add(nums[i])
        #
        # return False

        # bucket solution from LC
        #
        # # Bucket sort. Each bucket has size of t. For each number, the possible
        # # candidate can only be in the same bucket or the two buckets besides.
        # # Keep as many as k buckets to ensure that the difference is at most k.
        # buckets = {}
        # for i, v in enumerate(nums):
        #     # t == 0 is a special case where we only have to check the bucket
        #     # that v is in.
        #     bucketNum, offset = (v / t, 1) if t else (v, 0)
        #     for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
        #         if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
        #             return True
        #
        #     buckets[bucketNum] = nums[i]
        #     if len(buckets) > k:
        #         # Remove the bucket which is too far away. Beware of zero t.
        #         del buckets[nums[i - k] / t if t else nums[i - k]]
        #
        # return False


start_time = time()

_nums = [1,2,3,1]
_indexDiff = 3
_valueDiff = 0
# Example 1:
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
#
# Example 2:
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.

print(Solution().containsNearbyAlmostDuplicate(_nums, _indexDiff, _valueDiff))

print("--- %s seconds ---" % (time() - start_time))