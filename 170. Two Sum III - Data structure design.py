from collections import defaultdict


class TwoSum:

    # after reading documentation
    #
    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for number, col in self.nums.items():
            target = value - number
            if number == target:
                if self.nums[number] > 1:
                    return True
            elif target in self.nums:
                return True
        return False

# my first solution, slow
#
#     def __init__(self):
#         self.nums = set()
#         self.sums = set()
#
#     def add(self, number: int) -> None:
#         for num in self.nums:
#             self.sums.add(num + number)
#         self.nums.add(number)
#
#     def find(self, value: int) -> bool:
#         return value in self.sums


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)