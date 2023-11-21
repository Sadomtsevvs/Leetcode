from collections import defaultdict
from time import time
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        d = defaultdict(int)
        stack = []
        for log in logs:
            num, event, time = log.split(':')
            time = int(time)
            if event == 'start':
                stack.append((time, 0))
            else:
                start, add = stack.pop()
                period = time - start + 1 - add
                d[int(num)] += period
                if stack:
                    add += period
                    stack[-1] = stack[-1][0], stack[-1][1] + add
        return [d[i] for i in range(n)]

        # from comments
        #
        # def exclusiveTime(self, N, logs):
        #     ans = [0] * N
        #     stack = []
        #     prev_time = 0
        #
        #     for log in logs:
        #         fn, typ, time = log.split(':')
        #         fn, time = int(fn), int(time)
        #
        #         if typ == 'start':
        #             if stack:
        #                 ans[stack[-1]] += time - prev_time
        #             stack.append(fn)
        #             prev_time = time
        #         else:
        #             ans[stack.pop()] += time - prev_time + 1
        #             prev_time = time + 1
        #
        #     return ans


start_time = time()

# Example 1:
# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]
# Explanation:
# Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
# Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
# Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
# So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
#
# Example 2:
# Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# Output: [8]
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
# Function 0 (initial call) resumes execution then immediately calls itself again.
# Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
# Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
# So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
#
# Example 3:
# Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
_n = 2
_logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
# Output: [7,1] Explanation: Function 0 starts at the beginning of time 0, executes for 2 units of time,
# and recursively calls itself. Function 0 (recursive call) starts at the beginning of time 2 and executes for 4
# units of time. Function 0 (initial call) resumes execution then immediately calls function 1. Function 1 starts at
# the beginning of time 6, executes 1 unit of time, and ends at the end of time 6. Function 0 resumes execution at
# the beginning of time 6 and executes for 2 units of time. So function 0 spends 2 + 4 + 1 = 7 units of total time
# executing, and function 1 spends 1 unit of total time executing.

print(Solution().exclusiveTime(_n, _logs))

print("--- %s seconds ---" % (time() - start_time))
