# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(0, head)
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy.next


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

_head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
_head = Solution().deleteDuplicates(_head)
print(_head)