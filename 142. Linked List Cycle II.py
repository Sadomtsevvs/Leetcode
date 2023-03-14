# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow

        # my future solution
        #
        # if not head or not head.next:
        #     return None
        # slow = head.next
        # fast = head.next.next
        # while slow != fast and fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # if not fast or not fast.next:
        #     return None
        # slow = head
        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next
        # return slow
