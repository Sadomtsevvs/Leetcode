from time import time
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = []
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        for i in range(k):
            part = head
            num, rest = divmod(n, k - i)
            if rest > 0:
                num += 1
            n -= num
            prev = head
            for _ in range(num):
                prev, head = head, head.next
            if prev:
                prev.next = None
            result.append(part)
        return result


start_time = time()

# Example 1:
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
#
# Example 2:
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
_head = [1,2,3,4,5,6,7,8,9,10]
_k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

print(Solution().splitListToParts(_head, _k))

print("--- %s seconds ---" % (time() - start_time))
