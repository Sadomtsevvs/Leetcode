from time import time
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        for i in range(len(nums)):
            nums[i] = int(nums[i], 2)
        nums = set(nums)
        num = 0
        while True:
            if num not in nums:
                ans = str(bin(num))[2:]
                if len(ans) < len(nums):
                    ans = '0' * (len(nums) - len(ans)) + ans
                return ans
            num += 1

        # great solution from editorial
        #
        # ans = []
        # for i in range(len(nums)):
        #     curr = nums[i][i]
        #     ans.append("1" if curr == "0" else "0")
        # return "".join(ans)


start_time = time()

# Example 1:
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct
#
# Example 2:
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
#
# Example 3:
# Input: nums = ["111","011","001"]
_nums = nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

print(Solution().findDifferentBinaryString(_nums))

print("--- %s seconds ---" % (time() - start_time))