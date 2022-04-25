# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        if not head.next:
            return True
        # seeking for middle and reverse first half of the list
        prev = None
        slow_next = head.next
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow.next = prev
            prev = slow
            slow = slow_next
            slow_next = slow_next.next
        # begin-node depends on the length list parity
        if fast:
            slow = slow.next
        while slow:
            if slow.val != prev.val:
                return False
            else:
                slow = slow.next
                prev = prev.next
        return True

        # pretty solution from LC comments, looks like mine but more elegant
        #
        # rev = None
        # slow, fast = head, head
        #
        # while fast and fast.next:
        #     fast = fast.next.next
        #     rev, rev.next, slow = slow, rev, slow.next
        #
        # if fast:
        #     slow = slow.next
        #
        # while rev and rev.val == slow.val:
        #     rev, slow = rev.next, slow.next
        #
        # return not rev

_head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
print(Solution().isPalindrome(_head))
pass