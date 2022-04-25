# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_passed = set()
        cur = headA
        while cur:
            a_passed.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in a_passed:
                return cur
            cur = cur.next
        return None


# O(1) memory solution from LC comments
#
# class Solution:
#     # two linkedlist
#     # use hashset could solve this question
#     # but it will introduce extra space
#     # The ideal way - "connect" these two linkedlist
#     # use p1, p2 - starts from headA and headB firstly
#     # then when p1 finished listA, move to listB
#     # vice versa for p2
#     # e.g.
#     # 4,1,8,4,5|5,6,1,8,4,5
#     # 5,6,1,8,4,5|4,1,8,4,5
#     #                 |
#     # intersect at 8
#     # if there is no intersection
#     # p1 and p2 will be None and p1 == p2 -> then return any one of them will be ok
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         p1, p2 = headA, headB
#
#         while p1 != p2:
#             p1 = p1.next if p1 is not None else headB
#             p2 = p2.next if p2 is not None else headA
#
#         return p1
