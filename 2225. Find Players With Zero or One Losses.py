from time import time


class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        current_min = int(current[:2])*60 + int(current[3:])
        correct_min = int(correct[:2])*60 + int(correct[3:])

        result = 0

        while correct_min != current_min:
            if correct_min - current_min >= 60:
                current_min += 60
            elif correct_min - current_min >= 15:
                current_min += 15
            elif correct_min - current_min >= 5:
                current_min += 5
            else:
                current_min += 1
            result += 1
        return result


start_time = time()

_current = "02:30"
_correct = "04:35"
# Input: current = "02:30", correct = "04:35"
# Output: 3
# Explanation:
# We can convert current to correct in 3 operations as follows:
# - Add 60 minutes to current. current becomes "03:30".
# - Add 60 minutes to current. current becomes "04:30".
# - Add 5 minutes to current. current becomes "04:35".
# It can be proven that it is not possible to convert current to correct in fewer than 3 operations.

print(Solution().convertTime(_current, _correct))

print("--- %s seconds ---" % (time() - start_time))
