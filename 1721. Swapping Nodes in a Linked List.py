# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k: int):

        # first we'll find the k node and length
        pre_k_node, k_node = None, None
        pre_node, cur_node = None, head
        cur_pos = 1
        while cur_node:
            if cur_pos == k:
                pre_k_node = pre_node
                k_node = cur_node
            pre_node = cur_node
            cur_node = cur_node.next
            cur_pos += 1

        len_list = cur_pos - 1

        # check if is it middle, then no swap needed
        if len_list % 2 == 1 and k == len_list // 2 + 1:
            return head

        # second we'll find the (len - k) node
        kl_node, pre_kl_node = None, None
        pre_node, cur_node = None, head
        cur_pos = 1
        while cur_node:
            if cur_pos == len_list - k + 1:
                pre_kl_node = pre_node
                kl_node = cur_node
                break
            pre_node = cur_node
            cur_node = cur_node.next
            cur_pos += 1

        if k > len_list - k + 1:
            k_node, kl_node = kl_node, k_node
            pre_k_node, pre_kl_node = pre_kl_node, pre_k_node

        if pre_k_node is not None:
            pre_k_node.next = kl_node

        if pre_kl_node is not None:
            pre_kl_node.next = k_node

        k_node.next, kl_node.next = kl_node.next, k_node.next

        if pre_k_node is None:
            head = kl_node

        return head

        # solution from LC comments
        #
        # n = 0
        # beg = head
        # while beg:
        #     if n == k - 1: l = beg
        #     beg = beg.next
        #     n += 1
        #
        # r = head
        # for m in range(n - k):
        #     r = r.next
        #
        # l.val, r.val = r.val, l.val
        # return head

print(Solution().swapNodes(ListNode(1, ListNode(2)), 1))
