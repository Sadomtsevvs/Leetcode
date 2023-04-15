from time import time
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pos_pop = 0
        for char in pushed:
            if char == popped[pos_pop]:
                pos_pop += 1
            else:
                stack.append(char)
            while stack and stack[-1] == popped[pos_pop]:
                stack.pop()
                pos_pop += 1
        return len(stack) == 0


start_time = time()

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
_pushed = [1,2,3,4,5]
_popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
_pushed = [1,2,3,4,5]
_popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

_pushed = [0,2,1]
_popped = [0,1,2]

_pushed = [2,1,0]
_popped = [1,2,0]


print(Solution().validateStackSequences(_pushed, _popped))

print("--- %s seconds ---" % (time() - start_time))
