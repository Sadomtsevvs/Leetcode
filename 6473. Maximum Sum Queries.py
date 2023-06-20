from time import time
from typing import List


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # brute-force O(n*q)
        #
        # result = []
        # for x, y in queries:
        #     s = -1
        #     for i in range(len(nums1)):
        #         if nums1[i] >= x and nums2[i] >= y:
        #             s = max(s, nums1[i] + nums2[i])
        #     result.append(s)
        # return result

        max_num1 = 0
        max_num2 = 0

        xarr = []
        yarr = []
        for i in range(len(nums1)):
            num1, num2 = nums1[i], nums2[i]
            xarr.append((num1, num2, num1 + num2, i))
            yarr.append((num1, num2, num1 + num2, i))
            max_num1 = max(max_num1, num1)
            max_num2 = max(max_num2, num2)

        xarr.sort(reverse=True, key=lambda x: x[0])
        yarr.sort(reverse=True, key=lambda x: x[1])

        mxx = []
        cur_max = -1
        for i in range(len(nums1)):
            cur_max = max(cur_max, xarr[i][2])
            mxx.append(cur_max)

        mxy = []
        cur_max = -1
        for i in range(len(nums1)):
            cur_max = max(cur_max, yarr[i][2])
            mxy.append(cur_max)

        result = []
        for x, y in queries:
            if x > max_num1:
                result.append(-1)
                continue
            if y > max_num2:
                result.append(-1)
                continue
            beg, end = 0, len(nums1)-1
            while beg <= end:
                mid = (beg + end) // 2
                if xarr[mid][0] >= x:
                    beg = mid + 1
                else:
                    end = mid - 1
            ind1 = beg - 1
            beg, end = 0, len(nums1)-1
            while beg <= end:
                mid = (beg + end) // 2
                if yarr[mid][1] >= y:
                    beg = mid + 1
                else:
                    end = mid - 1
            ind2 = beg - 1
            result.append(min(mxx[ind1], mxy[ind2]))

        return result


start_time = time()


# Example 1:
# Input: nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
_nums1 = [4,3,1,2]
_nums2 = [2,4,9,5]
_queries = [[4,1],[1,3],[2,5]]
# Output: [6,10,7]
# Explanation:
# For the 1st query xi = 4 and yi = 1, we can select index j = 0 since nums1[j] >= 4 and nums2[j] >= 1. The sum nums1[j] + nums2[j] is 6, and we can show that 6 is the maximum we can obtain.
# For the 2nd query xi = 1 and yi = 3, we can select index j = 2 since nums1[j] >= 1 and nums2[j] >= 3. The sum nums1[j] + nums2[j] is 10, and we can show that 10 is the maximum we can obtain.
# For the 3rd query xi = 2 and yi = 5, we can select index j = 3 since nums1[j] >= 2 and nums2[j] >= 5. The sum nums1[j] + nums2[j] is 7, and we can show that 7 is the maximum we can obtain.
# Therefore, we return [6,10,7].
#
# Example 2:
# Input: nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
# _nums1 = [3,2,5]
# _nums2 = [2,3,4]
# _queries = [[4,4],[3,2],[1,1]]
# Output: [9,9,9]
# Explanation: For this example, we can use index j = 2 for all the queries since it satisfies the constraints for each query.
#
# Example 3:
# Input: nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]
# _nums1 = [2,1]
# _nums2 = [2,3]
# _queries = [[3,3]]
# Output: [-1]
# Explanation: There is one query in this example with xi = 3 and yi = 3. For every index, j, either nums1[j] < xi or nums2[j] < yi. Hence, there is no solution.

# Input:
# [76,39]
# [29,42]
# [[75,34]]
# Output:
# [105]
# Expected:
# [-1]

_nums1 = [76,39]
_nums2 = [29,42]
_queries = [[75,34]]

print(Solution().maximumSumQueries(_nums1, _nums2, _queries))

print("--- %s seconds ---" % (time() - start_time))
