# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = ''
        while head:
            result += str(head.val)
            head = head.next
        return int(result, 2)

        # official solution 1
        # 
        # num = head.val
        # while head.next:
        #     num = num * 2 + head.next.val
        #     head = head.next
        # return num

        # official solution 2
        # 
        # num = head.val
        # while head.next:
        #     num = (num << 1) | head.next.val
        #     head = head.next
        # return num