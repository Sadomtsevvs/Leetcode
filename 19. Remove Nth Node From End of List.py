# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # my second solution, using two pointers
        prev = None
        cur, cand = head, head
        index = 1
        while cur:
            if index > n:
                prev = cand
                cand = cand.next
            index += 1
            cur = cur.next
        if cand == head:
            head = head.next
        else:
            prev.next = cand.next
        return head

        # my first solution
        #
        # node = head
        # depth = 1
        # while node.next is not None:
        #     depth += 1
        #     node = node.next
        # delete = depth - n
        # if delete == 0:
        #     return head.next
        # node = head
        # prev_node = None
        # for i in range(delete):
        #     prev_node = node
        #     node = node.next
        # prev_node.next = node.next
        # return head

        # Pochmann solution
        #
        # fast = slow = head
        # for _ in range(n):
        #     fast = fast.next
        # if not fast:
        #     return head.next
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head