from time import time


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        head = Node(1)
        cur = head
        for i in range(2, n + 1):
            cur.next = Node(i)
            cur = cur.next
        cur.next = head
        count = 1
        while head != head.next:
            if k - count == 1:
                count = 1
                head.next = head.next.next
            else:
                count += 1
            head = head.next
        return head.val

        # solution from LC comments
        #
        # res = 0
        # for size in range(2, n + 1):
        #     res = (k + res) % size
        # return res + 1


start_time = time()

_n = 5
_k = 2
# Input: n = 5, k = 2
# Output: 3
# Explanation: Here are the steps of the game:
# 1) Start at friend 1.
# 2) Count 2 friends clockwise, which are friends 1 and 2.
# 3) Friend 2 leaves the circle. Next start is friend 3.
# 4) Count 2 friends clockwise, which are friends 3 and 4.
# 5) Friend 4 leaves the circle. Next start is friend 5.
# 6) Count 2 friends clockwise, which are friends 5 and 1.
# 7) Friend 1 leaves the circle. Next start is friend 3.
# 8) Count 2 friends clockwise, which are friends 3 and 5.
# 9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

print(Solution().findTheWinner(_n, _k))

print("--- %s seconds ---" % (time() - start_time))
