# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:

        # iterative
        if not head:
            return head
        tail = head
        while head.next:
            next_tail = head.next
            head.next = next_tail.next
            next_tail.next = tail
            tail = next_tail
        return tail

        # recursion, not my code
        # if not head or not head.next:
        #     return head
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p


_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(Solution().reverseList(_head))
