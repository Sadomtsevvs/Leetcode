# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        length = 1
        cur = head
        while cur.next is not None:
            length += 1
            cur = cur.next
        k %= length
        if k == 0:
            return head
        cur.next = head
        index = 1
        cur = head
        while index < length - k:
            index += 1
            cur = cur.next
        head = cur.next
        cur.next = None
        return head