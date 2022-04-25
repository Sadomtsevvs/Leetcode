# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        prev_odd = head
        first_even = head.next
        cur = head.next
        while cur and cur.next:
            prev_odd.next = cur.next
            prev_odd = prev_odd.next
            cur.next = prev_odd.next
            # prev_odd.next = first_even # this line can be moved out of cycle
            cur = cur.next
        prev_odd.next = first_even  # !
        return head


_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
_newhead = Solution().oddEvenList(_head)
pass
