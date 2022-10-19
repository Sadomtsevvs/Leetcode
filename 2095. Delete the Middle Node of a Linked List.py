# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow, fast = ListNode(0, head), head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head

        # official solution - they don't use dummy node
        #
        # # Edge case: return None if there is only one node.
        # if head.next == None:
        #     return None
        #
        # # Initialize two pointers, 'slow' and 'fast'.
        # slow, fast = head, head.next.next
        #
        # # Let 'fast' move forward by 2 nodes, 'slow' move forward by 1 node each step.
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #
        # # When 'fast' reaches the end, remove the next node of 'slow' and return 'head'.
        # slow.next = slow.next.next
        #
        # # The job is done, return 'head'.
        # return head