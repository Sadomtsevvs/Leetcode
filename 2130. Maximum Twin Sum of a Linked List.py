# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # straightforward solution
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        ans = 0
        n = len(nums)
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n-i-1])
        return ans

        # nice solution from LC
        #
        # slow, fast = head, head
        # maxVal = 0
        #
        # # Get middle of linked list
        # while fast:
        #     fast = fast.next.next
        #     slow = slow.next
        #
        # # Reverse second part of linked list
        # curr, prev = slow, None
        #
        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next
        #
        # # Get max sum of pairs
        # while prev:
        #     maxVal = max(maxVal, head.val + prev.val)
        #     prev = prev.next
        #     head = head.next
        #
        # return maxVal
