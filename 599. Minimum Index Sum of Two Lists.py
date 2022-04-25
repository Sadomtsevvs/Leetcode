from time import time


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        min_index = float('inf')
        # like1 = {}
        # for i in range(len(list1)):
        #     like1[list1[i]] = i
        like1 = {val: i for i, val in enumerate(list1)}
        like_both = {}
        for i in range(len(list2)):
            if list2[i] in like1:
                like_both[list2[i]] = like1[list2[i]] + i
                min_index = min(min_index, like_both[list2[i]])
        # result = []
        # for restaurant, index in like_both.items():
        #     if index == min_index:
        #         result.append(restaurant)
        # return result
        return [restaurant for restaurant, index in like_both.items() if index == min_index]


start_time = time()

_list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
_list2 = ["KFC","Shogun","Burger King"]
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

print(Solution().findRestaurant(_list1, _list2))

print("--- %s seconds ---" % (time() - start_time))
