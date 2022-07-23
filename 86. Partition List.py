# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.val >= x:
                break
            prev, head = head, head.next
        tail = prev
        while head:
            if head.val < x:
                prev.next = head.next
                head.next = tail.next
                tail.next = head
                tail = tail.next
                head = prev.next
            else:
                prev, head = head, head.next
        return dummy.next

        # official solution
        #
        # before = before_head = ListNode(0)
        # after = after_head = ListNode(0)
        #
        # while head:
        #     # If the original list node is lesser than the given x,
        #     # assign it to the before list.
        #     if head.val < x:
        #         before.next = head
        #         before = before.next
        #     else:
        #         # If the original list node is greater or equal to the given x,
        #         # assign it to the after list.
        #         after.next = head
        #         after = after.next
        #
        #     # move ahead in the original list
        #     head = head.next
        #
        # # Last node of "after" list would also be ending node of the reformed list
        # after.next = None
        # # Once all the nodes are correctly assigned to the two lists,
        # # combine them to form a single list which would be returned.
        # before.next = after_head.next
        #
        # return before_head.next
