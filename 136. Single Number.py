from time import time


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # You must implement a solution with a linear runtime complexity and use only constant extra space.
        storage = set()
        for i in nums:
            if i in storage:
                storage.remove(i)
            else:
                storage.add(i)
        return storage.pop()

        # genius solution from LC comments
        # Intuition:
        # Xor of any two num gives the difference of bit as 1 and same bit as 0.
        # Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
        # So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
        # Time: O(n)
        # Space: O(1)
        #
        # xor = 0
        # for num in nums:
        #     xor ^= num
        # return xor



start_time = time()

_nums = [4, 1, 2, 1, 2]
# Input: nums = [4,1,2,1,2]
# Output: 4

print(Solution().singleNumber(_nums))

print("--- %s seconds ---" % (time() - start_time))
