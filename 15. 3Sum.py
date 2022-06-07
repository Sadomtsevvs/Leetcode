from time import time


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = set()
        nums.sort()
        prev = None

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if nums[i] == prev:
                continue
            prev = nums[i]
            target = 0 - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right and nums[right] >= 0:
                s = nums[left] + nums[right]
                if s == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return list(map(list, result))


        # my first solution, it works, but slow
        #
        # result = []
        # result_sets = set()
        # nums_dict = {}
        # for num in nums:
        #     if nums_dict.get(num) is None:
        #         nums_dict[num] = 1
        #     else:
        #         nums_dict[num] += 1
        # for i in range(len(nums) - 2):
        #     nums_dict[nums[i]] -= 1
        #     for j in range(i+1, len(nums) - 1):
        #         nums_dict[nums[j]] -= 1
        #         seek = 0 - nums[i] - nums[j]
        #         num_k = nums_dict.get(seek)
        #         if num_k is not None and num_k > 0:
        #             if {nums[i], nums[j], seek} not in result_sets:
        #                 result.append([nums[i], nums[j], seek])
        #                 result_sets.add(frozenset([nums[i], nums[j], seek]))
        #     for j in range(i+1, len(nums) - 1):
        #         nums_dict[nums[j]] += 1
        # return result

        # Solution from LC comments
        #
        # res = []
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     if nums[i] > 0:
        #         break
        #     l, r = i+1, len(nums)-1
        #     while l < r:
        #         s = nums[i] + nums[l] + nums[r]
        #         if s < 0:
        #             l +=1
        #         elif s > 0:
        #             r -= 1
        #         else:
        #             res.append((nums[i], nums[l], nums[r]))
        #             while l < r and nums[l] == nums[l+1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r-1]:
        #                 r -= 1
        #             l += 1; r -= 1
        # return res

    # Solution from LC comments
    #
    #     # a + b + c = 0
    #     triplets = []
    #     nums = sorted(nums)
    #     used_a = set()
    #
    #     for i in range(0, len(nums) - 2):
    #         a, b, c = nums[i], nums[i + 1], nums[i + 2]
    #         if a in used_a:
    #             continue
    #         else:
    #             used_a.add(a)
    #
    #         # a + b + c = 0
    #         # b + c = -a
    #         target = -1 * a
    #
    #         match = self.twoSum(nums[i + 1:], target)
    #         if match:
    #             for m in match:
    #                 triplets.append([a, m[0], m[1]])
    #
    #     return triplets
    #
    # ## Copied from Two-Sum II Solution
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     l, r = 0, len(numbers) - 1
    #     found = []
    #     used = set()
    #     while l < r:
    #         current_val = target - (numbers[l] + numbers[r])
    #         if current_val == 0:
    #             if numbers[l] not in used:
    #                 used.add(numbers[l])
    #                 found.append((numbers[l], numbers[r]))
    #             l += 1
    #         elif current_val < 0:
    #             r -= 1
    #         else:
    #             l += 1
    #     return found



start_time = time()

_nums = [3, 0, -2, -1, 1, 2]
#_nums = [0, 0, 0, 0]
_nums = [-1,0,1,2,-1,-4]
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

print(Solution().threeSum(_nums))

print("--- %s seconds ---" % (time() - start_time))
