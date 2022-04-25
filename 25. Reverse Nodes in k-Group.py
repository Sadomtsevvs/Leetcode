# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):

        if k == 1:
            return head

        def reverse_nodes(prev, head):
            next = head.next.next
            head.next.next = prev.next
            prev.next = head.next
            head.next = next

        dummy = ListNode(0, head)
        prev = dummy
        while head and head.next:
            i = 1
            while i < k and head.next:
                reverse_nodes(prev, head)
                i += 1
            if i < k:
                # last group need to be re-reverse
                head = prev.next
                j = 1
                while j < i:
                    reverse_nodes(prev, head)
                    j += 1
                break
            prev = head
            head = head.next
        return dummy.next


_root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
_k = 3
_new_root = Solution().reverseKGroup(_root, _k)
pass