# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        cur = 1
        while cur < left:
            cur += 1
            prev = head
            head = head.next
        for i in range(right-left):
            next = head.next
            head.next = next.next
            next.next = prev.next
            prev.next = next
        return dummy.next


