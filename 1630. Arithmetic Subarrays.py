from time import time
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for m in range(len(l)):
            beg, end = l[m], r[m]
            if end - beg == 1:
                ans.append(True)
                continue
            arr = nums[beg:end+1]
            arr.sort()
            delta = arr[1] - arr[0]
            for i in range (2, len(arr)):
                if arr[i] - arr[i-1] != delta:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans


start_time = time()

# Example 1:
# Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
# Output: [true,false,true]
# Explanation:
# In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
# In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
# In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
#
# Example 2:
# Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
_nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
_l = [0,1,6,4,8,7]
_r = [4,4,9,7,9,10]
# Output: [false,true,false,false,true,true]

print(Solution().checkArithmeticSubarrays(_nums, _l, _r))

print("--- %s seconds ---" % (time() - start_time))
