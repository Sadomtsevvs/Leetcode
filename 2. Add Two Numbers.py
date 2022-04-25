# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = num2 =''
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next
        res = int(num1[::-1]) + int(num2[::-1])
        res_list = list(map(int, str(res)))
        node, prev = None, None
        for i in range(len(res_list)):
            node = ListNode(res_list[i], prev)
            prev = node
        return node

        # pretty solution from LC comments
        #
        # dummy = ListNode()
        # curr = dummy
        # carry = 0
        #
        # while l1 or l2 or carry:
        #     v1 = l1.val if l1 else 0
        #     v2 = l2.val if l2 else 0
        #
        #     # new digit
        #     val = v1 + v2 + carry
        #     carry = val // 10
        #     val = val % 10
        #     curr.next = ListNode(val)
        #
        #     # updating pointers
        #     curr = curr.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        # return dummy.next


    # def pylist_to_listnode(self, pylist, link_count):
    #     if len(pylist) > 1:
    #         ret = precompiled.listnode.ListNode(pylist.pop())
    #         ret.next = self.pylist_to_listnode(pylist, link_count)
    #         return ret
    #     else:
    #         return precompiled.listnode.ListNode(pylist.pop(), None)
    #
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     num1 = num2 = ''
    #     while True:
    #         num1 += str(l1.val)
    #         if l1.next == None:
    #             break
    #         l1 = l1.next
    #     while True:
    #         num2 += str(l2.val)
    #         if l2.next == None:
    #             break
    #         l2 = l2.next
    #     res = int(num1[::-1]) + int(num2[::-1])
    #     res_list = list(map(int, str(res)))
    #     return (self.pylist_to_listnode(res_list, len(res_list)))


_l1 = ListNode(2, ListNode(4, ListNode(3)))
_l2 = ListNode(5, ListNode(6, ListNode(4)))
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

result = Solution().addTwoNumbers(_l1, _l2)
pass
