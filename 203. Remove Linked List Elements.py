# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        prev = head
        cur = head.next
        while cur:
            if cur.val == val:
                while cur and cur.val == val:
                    cur = cur.next
                prev.next = cur
                if not cur:
                    break
            prev = cur
            cur = cur.next
        return head