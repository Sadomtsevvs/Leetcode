# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # my second solution
        #
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next
        return slow == fast

        # my first solution
        #
        # if not head:
        #     return False
        # slow = head
        # fast = head.next
        # while slow.next and fast.next and fast.next.next and slow != fast:
        #     slow = slow.next
        #     fast = fast.next.next
        # if slow == fast:
        #     return True
        # return False

        # also nice solution from LC comments
        #
        # slow, fast = head, head
        #
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        #
        # return False
