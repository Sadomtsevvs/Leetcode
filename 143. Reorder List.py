# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        reverse_head = head
        cur = head
        len = 1
        while cur.next:
            reverse_head = ListNode(cur.next.val, reverse_head)
            cur = cur.next
            len += 1
        dummy = ListNode(0, head)
        l = 0
        while l < len:
            next, r_next = head.next, reverse_head.next
            head.next = reverse_head
            head.next.next = next
            reverse_head = r_next
            l += 2
            if l == len:
                head.next.next = None
            elif l > len:
                head.next = None
            else:
                head = next
        head = dummy.next

        # solution from LC comments
        #
        # # step 1: find middle
        # if not head: return []
        # slow, fast = head, head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #
        # # step 2: reverse second half
        # prev, curr = None, slow.next
        # while curr:
        #     nextt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextt
        # slow.next = None
        #
        # # step 3: merge lists
        # head1, head2 = head, prev
        # while head2:
        #     nextt = head1.next
        #     head1.next = head2
        #     head1 = head2
        #     head2 = nextt


# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

_root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# _root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(_root)
pass