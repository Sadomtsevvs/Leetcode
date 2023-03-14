from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode], first_index=0, last_index=None) -> Optional[TreeNode]:
        if not head:
            return None
        if last_index == -1:
            return None
        if last_index is None:
            last_index = -1
            node = head
            while node:
                node = node.next
                last_index += 1
        if first_index > last_index:
            return None
        cur = first_index
        node = head
        while cur < (first_index + last_index) // 2:
            node = node.next
            cur += 1
        return TreeNode(node.val, self.sortedListToBST(head, first_index, cur - 1),
                        self.sortedListToBST(node.next, cur + 1, last_index))


# _head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
_head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
_tree = Solution().sortedListToBST(_head)
print(_tree)