# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        depth = 1
        while node.next is not None:
            depth += 1
            node = node.next
        middle = depth//2 + 1
        node = head
        for i in range(middle - 1):
            node = node.next
        return node

        # official solution 2
        # 
        # arr = [head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # return arr[len(arr) // 2]

        # official solution 2
        # 
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
