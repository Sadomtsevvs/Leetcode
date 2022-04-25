# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        result = n
        start = 1
        end = n
        while end >= start:
            mid = (end + start) // 2
            if isBadVersion(mid):
                result = min(result, mid)
                end = mid - 1
            else:
                start = mid + 1
        return result

        # official solution
        #
        # left = 1
        # right = n
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if isBadVersion(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left

