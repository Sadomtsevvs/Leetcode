# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list):

        # my first solution
        
        dummy = ListNode(0)
        node = dummy

        while True:
            min_val = float('inf')
            min_ind = -1
            to_remove = []
            for i in range(len(lists)):
                if lists[i] is None:
                    to_remove.append(i)
                    continue
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_ind = i

            if min_ind == -1:
                break

            node.next = lists[min_ind]
            node = node.next
            lists[min_ind] = lists[min_ind].next

            for i in reversed(to_remove):
                lists.pop(i)

        return dummy.next

    # solution from LC comments, cool
    #
    # def mergeKLists(self, lists):
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists) // 2
    #     l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
    #     return self.merge(l, r)
    #
    # def merge(self, l, r):
    #     dummy = p = ListNode()
    #     while l and r:
    #         if l.val < r.val:
    #             p.next = l
    #             l = l.next
    #         else:
    #             p.next = r
    #             r = r.next
    #         p = p.next
    #     p.next = l or r
    #     return dummy.next
    #
    # def merge1(self, l, r):
    #     if not l or not r:
    #         return l or r
    #     if l.val < r.val:
    #         l.next = self.merge(l.next, r)
    #         return l
    #     r.next = self.merge(l, r.next)
    #     return r

