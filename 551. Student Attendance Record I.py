from time import time


class Solution:
    def checkRecord(self, s: str) -> bool:
        num_abs = 0
        num_late = 0
        for char in s:
            if char == "A":
                num_late = 0
                num_abs += 1
                if num_abs > 1:
                    return False
            elif char == "L":
                num_late += 1
                if num_late > 2:
                    return False
            else:
                num_late = 0
        return True

        # LC 1
        #
        # return s.count('A') <= 1 and s.count('LLL') == 0

        # LC 2
        #
        # return s.count('A') <= 1 and 'LLL' not in s

start_time = time()

_s = "PPALLL"
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

print(Solution().checkRecord(_s))

print("--- %s seconds ---" % (time() - start_time))
