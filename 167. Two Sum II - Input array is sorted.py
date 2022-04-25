from time import time


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        ''' another solution
        for i in range(len(numbers) - 1):
            seek_for = target - numbers[i]
            start = i + 1
            end = len(numbers) - 1
            while end >= start:
                mid = (end + start) // 2
                if numbers[mid] == seek_for:
                    return [i + 1, mid + 1]
                elif numbers[mid] > seek_for:
                    end = mid - 1
                else:
                    start = mid + 1
        '''

start_time = time()

_numbers = [2, 3, 4, 15]
_target = 6

print(Solution().twoSum(_numbers, _target))

print("--- %s seconds ---" % (time() - start_time))
