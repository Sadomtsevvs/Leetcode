# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        good_node = ListNode(0, head)
        first_good_node = None
        while head and head.next:
            if head.val != head.next.val:
                good_node.next = head
                if first_good_node is None:
                    first_good_node = good_node.next
                good_node = good_node.next
                head = head.next
                continue
            while head.next and head.val == head.next.val:
                good_node.next = head.next.next
                head = head.next
            head = good_node.next
        if first_good_node is None:
            first_good_node = good_node.next
        return first_good_node

        # nice solution from LC
        #
        # dummy = cur = ListNode(0, head)
        #
        # while head:
        #     if head.next and head.val == head.next.val:
        #         while head.next and head.val == head.next.val:
        #             head = head.next
        #         cur.next = head.next
        #     else:
        #         cur = cur.next
        #     head = head.next
        #
        # return dummy.next

        # official solution
        #
        # # sentinel
        # sentinel = ListNode(0, head)
        #
        # # predecessor = the last node
        # # before the sublist of duplicates
        # pred = sentinel
        #
        # while head:
        #     # if it's a beginning of duplicates sublist
        #     # skip all duplicates
        #     if head.next and head.val == head.next.val:
        #         # move till the end of duplicates sublist
        #         while head.next and head.val == head.next.val:
        #             head = head.next
        #         # skip all duplicates
        #         pred.next = head.next
        #         # otherwise, move predecessor
        #     else:
        #         pred = pred.next
        #
        #         # move forward
        #     head = head.next
        #
        # return sentinel.next