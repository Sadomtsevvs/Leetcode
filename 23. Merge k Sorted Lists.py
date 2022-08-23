# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list):

        # my heap solution after reading official
        #
        dummy = ListNode(0)
        node = dummy

        heap = []

        for i in range(len(lists)):
            lst = lists[i]
            if lst:
                heapq.heappush(heap, (lst.val, i))

        while heap:
            val, idx = heapq.heappop(heap)
            lst = lists[idx]
            node.next = lst
            node = node.next
            lists[idx] = lists[idx].next
            lst = lists[idx]
            if lst:
                heapq.heappush(heap, (lst.val, idx))

        return dummy.next

        # my divide and conquer solution
        #
        # def merge(l, r):
        #     dummy = ListNode()
        #     node = dummy
        #     while l and r:
        #         if l.val <= r.val:
        #             node.next = l
        #             l = l.next
        #         else:
        #             node.next = r
        #             r = r.next
        #         node = node.next
        #     node.next = l or r
        #     return dummy.next
        #
        # if not lists:
        #     return None
        # if len(lists) == 1:
        #     return lists[0]
        # mid = len(lists) // 2
        # return merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))

        # my first solution
        #
        # dummy = ListNode(0)
        # node = dummy
        #
        # while True:
        #     min_val = float('inf')
        #     min_ind = -1
        #     to_remove = []
        #     for i in range(len(lists)):
        #         if lists[i] is None:
        #             to_remove.append(i)
        #             continue
        #         if lists[i].val < min_val:
        #             min_val = lists[i].val
        #             min_ind = i
        #
        #     if min_ind == -1:
        #         break
        #
        #     node.next = lists[min_ind]
        #     node = node.next
        #     lists[min_ind] = lists[min_ind].next
        #
        #     for i in reversed(to_remove):
        #         lists.pop(i)
        #
        # return dummy.next

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

